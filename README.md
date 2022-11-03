
  

<p  align="center">
<img  src="https://i.ibb.co/30LNpQz/feather-icon-1.png"  alt="Feather CLI"  border="0"/>
</p>

  

  

## Feather CLI

  

  

The **Feather CLI** is a python package that contains manage to feather erp.

  
  

### Install

```
$ pip install -i https://test.pypi.org/simple/ feather==0.0.1
```


#### Create Feather Application:
```
$ feather new -n ExampleApp -db ExampleDB -u user -p pass -h localhost -pt 5432
```
#### Options
-n, --name TEXT Name of feather applicatin
-db, --dbname TEXT Name of database
-u, --user TEXT Name of database user
-p, --userpass TEXT Password of database user
-h, --host TEXT Database address. default is localhost
-pt, --port INTEGER Port of database. default is 5432


### License

This project is licensed under the MIT License

### Feather ERP
[Feather ERP (http://feathererp.com)