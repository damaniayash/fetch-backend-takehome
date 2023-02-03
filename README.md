# fetch-backend-takehome
## Assumptions:
- The -ve points in the transaction incidate that the points are being spent.
- `transaction.csv` will be provided in the same directory as `transactions.py`
- You have python3 installed on your system, if not follow https://realpython.com/installing-python/

## Notes
- A sample transactions.csv has been provided, to use your own data make sure the filename is `transaction.csv` and is in the same directory as `transactions.py`
 - You can specify your own amount to spend by using the `-s`/`--spend` CLI arguement.
 - The program will display the output on console as well as create a json file with the name `payers.json` with the corresponding output.

## How to run this program
 - Open your command prompt/terminal, clone this repository and run the program.
 - `git clone https://github.com/damaniayash/fetch-backend-takehome.git`
 - `cd fetch-backend-takehome`
 - `python3 transactions.py -s 5000` / `python3 transactions.py --spend 5000`


