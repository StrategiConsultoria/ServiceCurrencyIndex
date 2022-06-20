# Grupo Strategi
## ServiceCurrencyIndex
> ipca, incc, igpm

### type csv
```
  GET /api/csv?index=ipca

  GET /api/csv?index=ipca&decimal=15

  GET /api/csv?start_year=2021&index=ipca

  GET /api/csv?end_year=2021&index=ipca
  
  GET /api/csv?start_month=5&index=ipca

  GET /api/csv?end_month=10&index=incc

  GET /api/csv?start_month=5&end_month=10&index=igpm

  GET /api/csv?end_year=2022&index=ipca
```
### type json
```
  GET /api/json?index=ipca

  GET /api/json?start_year=2021
  GET /api/json?start_year=2021&index=ipca


  GET /api/json?end_year=2021
  GET /api/json?end_year=2021&index=ipca
  
  GET /api/json?start_month=5
  GET /api/json?start_month=5&index=ipca

  GET /api/json?end_month=10
  GET /api/json?end_month=10&index=incc

  GET /api/json?start_month=5&end_month=10
  GET /api/json?start_month=5&end_month=10&index=igpm

  GET /api/json?end_year=2022
  GET /api/json?end_year=2022&index=ipca
```

| Parâmetro     | Type  | Options               | Description                         |
| :------------ | :---- | :-------------------- | :---------------------------------- |
| `index`       | `str` | `ipca or incc or igpm`| Return filter the index             |
| `start_year`  | `int` | `1 ... current year`  | Select start interval year          |
| `end_year`    | `int` | `1 ... current year`  | Select end interval year            |
| `start_month` | `int` | `1 ... 12`            | Select start interval month         |
| `end_month`   | `int` | `1 ... 12`            | Select end interval month           |
| `decimal`     | `int` | `1 ... 12...`         | Set decimal, default 6              |
