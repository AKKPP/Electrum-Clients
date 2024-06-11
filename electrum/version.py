from sys import platform as _platform

ELECTRUM_APP_VERSION = '1.0.3'

if _platform == "linux" or _platform == "linux2":
    ELECTRUM_VERSION = '1.0.3.2'
elif _platform == "darwin":
    ELECTRUM_VERSION = '1.0.3.3'
elif _platform == "win32":
    ELECTRUM_VERSION = '1.0.3.1'
elif _platform == "win64":
    ELECTRUM_VERSION = '1.0.3.1'
else:
    ELECTRUM_VERSION = '1.0.3.4'

APK_VERSION = '1.0.3.5'        # read by buildozer.spec

PROTOCOL_VERSION = '1.4'     # protocol version requested

# The hash of the mnemonic seed must begin with this
SEED_PREFIX        = '01'      # Standard wallet
SEED_PREFIX_SW     = '100'     # Segwit wallet
SEED_PREFIX_2FA    = '101'     # Two-factor authentication
SEED_PREFIX_2FA_SW = '102'     # Two-factor auth, using segwit


def seed_prefix(seed_type):
    if seed_type == 'standard':
        return SEED_PREFIX
    elif seed_type == 'segwit':
        return SEED_PREFIX_SW
    elif seed_type == '2fa':
        return SEED_PREFIX_2FA
    elif seed_type == '2fa_segwit':
        return SEED_PREFIX_2FA_SW
    raise Exception(f"unknown seed_type: {seed_type}")
