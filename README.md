# Grupo Strategi
## ServiceCurrencyIndex

###### type csv
```
  GET /csv?index=ipca

  GET /csv?start_year=2021&index=ipca

  GET /csv?end_year=2021&index=ipca
  
  GET /csv?start_month=5&index=ipca

  GET /csv?end_month=10&index=incc

  GET /csv?start_month=5&end_month=10&index=igmp

  GET /csv?end_year=2022&index=ipca
```
###### type json
```
  GET /json/
  GET /json?index=ipca

  GET /json?start_year=2021
  GET /json?start_year=2021&index=ipca


  GET /json?end_year=2021
  GET /json?end_year=2021&index=ipca
  
  GET /json?start_month=5
  GET /json?start_month=5&index=ipca

  GET /json?end_month=10
  GET /json?end_month=10&index=incc

  GET /json?start_month=5&end_month=10
  GET /json?start_month=5&end_month=10&index=igmp

  GET /json?end_year=2022
  GET /json?end_year=2022&index=ipca
```

| Parâmetro     | Type  | Options               | Description                         |
| :------------ | :---- | :-------------------- | :---------------------------------- |
| `index`      | `str` | `ipca or incc or igpm`| Return filter the index            |
| `start_year`  | `int` | `1 ... current year`  | Select start interval year          |
| `end_year`    | `int` | `1 ... current year`  | Select end interval year            |
| `start_month` | `int` | `1 ... 12`            | Select start interval month         |
| `end_month`   | `int` | `1 ... 12`            | Select end interval month           |


#### Start Server

```
python app.py
```
