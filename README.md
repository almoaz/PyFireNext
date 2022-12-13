# FireNext (Python)

FireNext is an offline database library.


## Authors

- [Mahfuz Salehin Moaz](https://www.github.com/almoaz)


## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/almoaz/FireNext/blob/master/LICENSE)
    
## Version 
1.0.1

## Installation
```
pip install firenext
```

## About FireNext

FireNext works with two types of offline databases. Table type and Document type. Table type database name "NextTable" and document type database name "NextDatabase".

## NextTable

```bash
id                  name                   phone 
------------------------------------------------------------
18301               Mithila Mithi          019XXXXXXXX
------------------------------------------------------------
18302               Mahfuz Salehin         017XXXXXXXX
------------------------------------------------------------
18303               Al Moaz                016XXXXXXXX

```

## NextDatabase

```bash
USER
   |---18301
   |       |---name:Mithila Nisa
   |       |---id:18301
   |       |---phone:019XXXXXXXX
   |---18302
   |       |---name:Mahfuz Salehin
   |       |---id:18302
   |       |---phone:017XXXXXXXX
   |---18303
   |       |---name:Al Moaz
   |       |---id:18303
   |       |---phone:016XXXXXXXX

```


## Documentation

- [NextTable (Python)](https://github.com/almoaz/FireNext/blob/master/NextTable.md)
- [NextDatabase (Python)](https://github.com/almoaz/FireNext/blob/master/NextDatabase.md)



## Restiction

Please do not use these characters in your documents.

- " Á " this character means database start tag
- " À " this character means database end tag
- " É " this character means database start tag
- " È " this character means database end tag
- " Ê " this character means database end tag
- " | " this character means add new data
- " : " this character means valueChild

"|" and ":" These character has its uses. You will find it in the documentation.


## Having problems?

Please inform me via email at 'almuaz1998@gmail.com'


## Thanks

- Many thanks' python developers
- Special Thanks to Future Next Developers
