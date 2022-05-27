# Grupo Strategi
## ServiceCurrencyIndex

###### type csv
```
  GET /csv?indice=ipca

  GET /csv?start_year=2021
  GET /csv?start_year=2021&indice=ipca

  GET /csv?end_year=2021
  GET /csv?end_year=2021&indice=ipca
  
  GET /csv?start_month=5
  GET /csv?start_month=5&indice=ipca

  GET /csv?end_month=10
  GET /csv?end_month=10&indice=incc

  GET /csv?start_month=5&end_month=10
  GET /csv?start_month=5&end_month=10&indice=igmp

  GET /csv?end_year=2022
  GET /csv?end_year=2022&indice=ipca
```
###### type json
```
  GET /json/
  GET /json?indice=ipca

  GET /json?start_year=2021
  GET /json?start_year=2021&indice=ipca


  GET /json?end_year=2021
  GET /json?end_year=2021&indice=ipca
  
  GET /json?start_month=5
  GET /json?start_month=5&indice=ipca

  GET /json?end_month=10
  GET /json?end_month=10&indice=incc

  GET /json?start_month=5&end_month=10
  GET /json?start_month=5&end_month=10&indice=igmp

  GET /json?end_year=2022
  GET /json?end_year=2022&indice=ipca
```

| Parâmetro     | Type  | Options               | Description                         |
| :------------ | :---- | :-------------------- | :---------------------------------- |
| `indice`      | `str` | `ipca or incc or igpm`| Return filter the indice            |
| `start_year`  | `int` | `1 ... current year`  | Select start interval year          |
| `end_year`    | `int` | `1 ... current year`  | Select end interval year            |
| `start_month` | `int` | `1 ... 12`            | Select start interval month         |
| `end_month`   | `int` | `1 ... 12`            | Select end interval month           |


#### Start Server

```
python app.py
```
