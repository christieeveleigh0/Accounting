
print("[Package] Banking package loaded.")

from banking.fvb.reconciliation import do_reconciliation as fvb_recon

# Update the __init__.py for the banking package to only auto-import the FVB (First Virtual Bank) module.