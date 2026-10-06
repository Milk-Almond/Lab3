#!/usr/bin/env python3
"""Validate saved artifacts, not model behavior. Uses only the standard library."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
AGENT = ROOT / 'agents/creation_agent'
SUPPORTED = {'$schema', 'title', 'type', 'required', 'properties', 'additionalProperties', 'items'}

def check_schema(schema):
    unsupported = set(schema) - SUPPORTED
    if unsupported:
        raise ValueError(f'Unsupported schema keywords: {unsupported}')
    for child in schema.get('properties', {}).values():
        check_schema(child)
    if 'items' in schema:
        check_schema(schema['items'])

def validate(value, schema, path='$'):
    kind = schema.get('type')
    types = {'object': dict, 'array': list, 'string': str}
    if kind not in types or not isinstance(value, types[kind]):
        raise ValueError(f'{path}: expected {kind}')
    if kind == 'object':
        missing = set(schema.get('required', [])) - value.keys()
        if missing:
            raise ValueError(f'{path}: missing {missing}')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False and set(value) - props.keys():
            raise ValueError(f'{path}: unexpected properties')
        for key, item in value.items():
            if key in props:
                validate(item, props[key], f'{path}.{key}')
    elif kind == 'array':
        for i, item in enumerate(value):
            validate(item, schema['items'], f'{path}[{i}]')

def run(*args):
    result = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)
    print('$ python ' + ' '.join(args))
    print(result.stdout.strip())
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)

run('tools/check_frozen_core.py')
input_schema = json.loads((ROOT/'core/input_schema.json').read_text())
output_schema = json.loads((ROOT/'core/output_schema.json').read_text())
for schema in [input_schema, output_schema]:
    check_schema(schema)
metadata = json.loads((AGENT/'agent_metadata.json').read_text())
for name in ['primary', 'contrast_1', 'boundary_missing_context']:
    case = json.loads((AGENT/'cases'/f'{name}.json').read_text())
    response_path = AGENT/'responses'/f'{name}_response.json'
    response = json.loads(response_path.read_text())
    validate(case, input_schema)
    validate(response, output_schema)
    assert response['agent'] == metadata, f'{name}: metadata mismatch'
    assert len(response['evidence']) == 6, f'{name}: incomplete source packet'
    for index, entry in enumerate(response['evidence'], start=1):
        assert entry['source_or_reference'].startswith(f'S{index}:')
    run('tools/validate_response.py', str(response_path.relative_to(ROOT)))
    with tempfile.TemporaryDirectory() as folder:
        regenerated = Path(folder)/'prompt.txt'
        result = subprocess.run([sys.executable, 'tools/build_prompt.py', '--agent', 'agents/creation_agent', '--case', f'agents/creation_agent/cases/{name}.json', '--out', str(regenerated)], cwd=ROOT, capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
        assert regenerated.read_bytes() == (AGENT/'records/prompts'/f'{name}.txt').read_bytes(), f'{name}: prompt drift'
    print(f'{name}: nested schema constraints, metadata, evidence IDs and prompt reproduction PASS')
for rel, expected in json.loads((AGENT/'records/test_artifact_sha256.json').read_text()).items():
    assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() == expected, f'Artifact changed: {rel}'
print('Artifact hashes PASS')
print('All saved-artifact checks PASS. Qualitative model behavior is reviewed separately; no model was invoked by this script.')
