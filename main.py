import os
from core import app
import sys
sys.dont_write_bytecode = True


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 11001))
    app.run(host='0.0.0.0', port=port)
