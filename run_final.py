#!/usr/bin/env python3
import os
import sys
os.chdir(r'c:\Users\Fo\Documents\danieldietrich.tech')
sys.path.insert(0, r'c:\Users\Fo\Documents\danieldietrich.tech')

# Run the translation
if __name__ == '__main__':
    try:
        # Import the final translation module
        import translate_final
        sys.exit(translate_final.main())
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
