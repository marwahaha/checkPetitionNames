README for matching names to addresses on a petition sheet.

These programs and scripts should help check signatures on petition
sheets against a file of registered voters. The problem is that the
sheets may only have signatures which are very hard to read. Looking
up addresses by hand is also cumbersome. In our case there are over
65,000 registered voters, and up to 250 signatures.

files discussed

1. only.tsv       -- tab separated abreviated voter registration file
2. test-sheet.tsv -- tab separated file of addresses
3. check.py       -- python source that reads these and prints out names
                     associated with each address. 

1. You need a voter file of registerd voters. For Proviso HSD 209 that
file is about 69752 lines long, and has about 25 columns.

for example the file I used had column headers

CERTNUM NAME TWP GRP ADDR_NUM ADDR_FRAC ADDR_DIR ADDR_STR ADDR_TYPE
ADDR_PDIR ADDR_OTHER ADDR_CITY STATE ADDR_ZIP BIRTHDATE age SEX REG_DT
after2011 LSTVOT_DT not voted last LAST_NAME FIRST_NAME MIDDLE_INI
SUFFIX SUID

(noticed I addes some fields -- lower case ones)

2. I only want the CERTNUM, name, address street number, direction,
street name and city.  So I preprocess the voter file to strip out
only those fields. Originally I had saved the voter file as tab
separated.

```
fr=RegisteredList.csv
cat $fr |awk -F"\t" '{print $1"\t"$2"\t"$5"\t"$7"\t"$8"\t"$12}' > only.tsv
```

Now only.tsv is tab separated and has just the fields I want.

3. make a file of the addresses you see on the petition sheet. Here is
an example

```
ADD	DIR	STR	CITY
123	N	35TH	NEWTON
456	E	MAIN	ELM PARK
...
```

It is also tab separated and uses exactly those headers.

4.1 Install python, and the library pandas. You probably have python
already installed.  to install pandas. The program uses python 2.7

4.2 Run the python program check.py which assumes the existence of
only.tsv in the current directory. It takes the address list file as
an argument.

python check.py test-sheet.tsv

5. The output looks like

```
macbook: $ python check.py test-sheet.tsv
123 N 35TH NEWTON
JONES, DANIEL
JONES, JESUS G
JONES, ROBERTO JR
JONES, ROSA MARIA
SMITH, JOSE LUIS
************

456 E MAIN ELM PARK
WOOD, JOSE P
STONE, CALIXTA
************
...
```

6. Now you can go down the list of signatures and try to match up with
names at the reported addresses.  And you can do this in the order
that the signatures and addresses are reported on the sheet, which
should make the job much easier.

7. We can cut and paste out the names who signed if we want to contact
them again.
