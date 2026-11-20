# Clinical Data Organizer

A beginner Python project that identifies synthetic patient records where asthma history was not documented.

## How it works

The script checks the `asthma_history` field in each record:

- `True` means the record states that the patient has a history of asthma.
- `False` means the record states that the patient has no history of asthma.
- `None` means asthma history was not documented.

The script returns only the IDs of records with `None`. It does not treat missing information as a negative finding.

## How to run

From the project folder, run:

```powershell
python main.py
```

No third-party packages are required.

## Example output

```text
['P003', 'P004']
Test passed!
```

## What the test checks

An `assert` statement checks that the sample output contains exactly `P003` and `P004`. The record with `False` is not included.

## Scope

This is a learning project using fictional records. It checks one field in structured data. It does not read clinical notes or make diagnoses.