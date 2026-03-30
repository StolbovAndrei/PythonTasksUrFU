import argparse
import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__name__)
        logger.info(f"Start reading file: args={args}, kwargs={kwargs}")
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            logger.error(f"File is not find")
            raise
        except PermissionError:
            logger.error(f"No access to file")
            raise
        except Exception as e:
            logger.error(f"Reading error: {e}")
            raise
    return wrapper

@logging_decorator
def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')

def head_generator(filename, num_lines):
    for i, line in enumerate(read_file_lines(filename)):
        if i >= num_lines:
            break
        yield line

def main():
    parser = argparse.ArgumentParser(
        description="Show the first N lines of file (analogous to POSIX head)"
    )
    parser.add_argument(
        '-n', '--lines',
        type=int,
        default=10,
        help="number of lines (default 10)"
    )
    parser.add_argument("filename", help="file to read")
    args = parser.parse_args()

    for line in head_generator(args.filename, args.lines):
        print(line)

if __name__ == '__main__':
    main()