import hashlib
import json

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given data.
    """

    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"cryptohash: {crypto_hash(6, 2, 3)}")
    print(f"cryptohash 2 3 6: {crypto_hash(2, 3, 6)}")
if __name__=="__main__":
    main()
