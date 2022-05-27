# Grupo Strategi
## Service Indice 

###### type csv
```
  GET /csv?indice=ipca
  
  GET /csv/2022?start_month=5
  GET /csv?indice=ipca&start_month=5

  GET /csv/2022?end_month=10
  GET /csv?indice=incc&end_month=10

  GET /csv/2022?start_month=5&end_month=10
  GET /csv?indice=igmp&start_month=5&end_month=10

  GET /csv/2021?end_year=2022
  GET /csv?indice=ipca&end_year=2022
```
###### type json
```
  GET /json/
  GET /json?indice=ipca
  
  GET /json/2022?start_month=5
  GET /json?indice=ipca&start_month=5

  GET /json/2022?end_month=10
  GET /json?indice=incc&end_month=10

  GET /json/2022?start_month=5&end_month=10
  GET /json?indice=igmp&start_month=5&end_month=10

  GET /json/2021?end_year=2022
  GET /json?indice=ipca&end_year=2022
```

| Parâmetro     | Type  | Options               | Description                         |
| :------------ | :---- | :-------------------- | :---------------------------------- |
| `indice`      | `str` | `ipca or incc or igpm`| Return filter the indice            |
| `start_month` | `int` | `1 ... 12`            | Select start interval month         |
| `end_month`   | `int` | `1 ... 12`            | Select end interval month           |
| `end_year`    | `int` | `1 ... current year`  | Select end interval year            |

#### Start Server

```
export FLASK_APP='server:create_app()'
flask run
```
