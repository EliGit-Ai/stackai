# Critical Blockers

A critical blocker is a condition that materially prevents a safe write-enabled Claude Code pilot.

Flag a blocker when one of these is true:

1. **No reliable source-code access**
   - The business cannot access the code required for the pilot.

2. **Ownership is unknown or vendor-only**
   - Critical repository or technical assets are solely controlled by an external vendor and the business cannot independently obtain them.

3. **Production-only change path**
   - There is no safe Development/Test path and changes would need to be performed directly in Production.

4. **No rollback**
   - There is no reliable Git history, backup, restore, or other rollback path appropriate to the planned work.

5. **No accountable internal owner**
   - Nobody in the business can approve the pilot, manage access, or make decisions with vendors.

6. **Critical credentials are inaccessible to the business**
   - Required production/deployment credentials exist only with a vendor or individual outside business control.

7. **Unmanaged sensitive data**
   - Sensitive data exists, but access, secrets, or credential handling is unknown or materially unsafe.

8. **Unsafe shared privileged access**
   - The operating model relies on shared administrator credentials with no traceability or ownership.

# Effect on recommendation

When a blocker exists:
- clearly name it
- explain why it matters
- recommend the minimum preparation step
- do not recommend broad write or Production access until resolved

A blocker does **not** necessarily prevent:
- read-only code analysis
- architecture mapping
- documentation
- ownership inventory
- vendor transition planning