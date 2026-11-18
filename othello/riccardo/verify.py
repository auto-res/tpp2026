"""Verify this documentary envelope; does not invoke Agda."""
import hashlib
import json
import sys
from pathlib import Path

def require(value, message):
    if not value:
        raise ValueError(message)

def verify(root):
    root = root.resolve()
    manifest = json.loads((root / 'SUBMISSION.json').read_text())
    require(manifest['format'] == 'tpp2026-review-envelope-v1', 'failed identity/status check')
    require(manifest['Problem3_complete'] is False, 'failed identity/status check')
    require(manifest['no_new_agda_check'] is True, 'failed identity/status check')
    require(manifest['email_sent'] is False, 'failed identity/status check')
    entries = manifest['files']
    require(isinstance(entries, dict) and len(entries) >= 20, 'failed identity/status check')
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    require(actual == set(entries) | {'SUBMISSION.json'}, 'missing or unexpected file')
    for name, rec in entries.items():
        rel = Path(name)
        require(not rel.is_absolute() and '..' not in rel.parts, 'failed identity/status check')
        p = root / rel
        require(not any(((root / Path(*rel.parts[:i])).is_symlink() for i in range(1, len(rel.parts) + 1))), name)
        data = p.read_bytes()
        require(type(rec['bytes']) is int and len(data) == rec['bytes'], name)
        require(hashlib.sha256(data).hexdigest() == rec['sha256'], name)
    completion = json.loads((root / 'problem2/evidence/completion.json').read_text())
    report = json.loads((root / 'problem2/evidence/theorem-report.json').read_text())
    checker = json.loads((root / 'problem2/evidence/checker-receipt.json').read_text())
    require(report['accepted'] is True and report['Problem2_checked'] is True, 'failed identity/status check')
    require(report['same_optimal_pair_black16_white20'] is True, 'failed identity/status check')
    require(checker['accepted'] is True and type(checker['exit_code']) is int and (checker['exit_code'] == 0), 'failed identity/status check')
    for key, name in [('actual_final_theorem_report', 'theorem-report.json'), ('actual_checker_record', 'checker-receipt.json'), ('source_audit', 'source-audit.json')]:
        p = root / 'problem2/evidence' / name
        require(hashlib.sha256(p.read_bytes()).hexdigest() == completion[key]['sha256'], key)
    print(json.dumps({'verified': True, 'indexed_files': len(entries), 'Problem3_complete': False, 'Agda_executed': False}))
if __name__ == '__main__':
    try:
        verify(Path(sys.argv[1] if len(sys.argv) > 1 else '.'))
    except Exception as exc:
        print('VERIFICATION FAILED: ' + str(exc), file=sys.stderr)
        sys.exit(1)
