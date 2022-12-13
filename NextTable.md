
## NextTable

NextTable work with 17 method 
-  NextTable.create_table()
-  NextTable.read_table()
-  NextTable.delete_table()
-  NextTable.add_col_name()
-  NextTable.read_col_name()
-  NextTable.update_col_name()
-  NextTable.delete_col_name()
-  NextTable.add_data()
-  NextTable.search_data()
-  NextTable.update_data()
-  NextTable.delete_data()
-  NextTable.search_row_data()
-  NextTable.update_row()
-  NextTable.delete_row()
-  NextTable.search_col_data()
-  NextTable.delete_col
-  NextTable.table_to_doc()


##  NextTable.create_table()
```bash
String tableName = "ducument";

NextTable.create_table(tableName);
```
```bash
Output: if table create succssfully you can find "tableName.nt" file. 
```


##  NextTable.read_table()
```bash
String tableName = "ducument";

NextTable.read_table(tableName);
```
```bash
Output: Table data.
```

##  NextTable.delete_table()
```bash
String tableName = "ducument";

NextTable.delete_table(tableName);
```

##  NextTable.add_col_name()
```bash
String tableName = "ducument";
String columnName = "id|name|phone";

NextTable.add_col_name(tableName, columnName);
```

##  NextTable.read_col_name()
```bash
String tableName = "ducument";

NextTable.read_col_name(tableName);

```
```bash
Output: Table column name.
```

##  NextTable.update_col_name()
```bash
String tableName = "ducument";
String columnName = "phone";
String updateColumnName = "email";

NextTable.update_col_name(tableName, columnName, updateColumnName);

```

##  NextTable.delete_col_name()
```bash
String tableName = "ducument";
String columnName = "phone";

NextTable.delete_col_name(tableName, columnName);
```

##  NextTable.add_data()
```bash
String tableName = "ducument";
String data = "18303|Al Moaz|016XXXXXXXX";

NextTable.add_data(tableName, data);
```

##  NextTable.search_data()
```bash
String tableName = "ducument";
String searchId = "18301";
String columnName = "phone";
NextTable.search_data(tableName, searchId, columnName);
```
```bash
Output: Search data.
```

##  NextTable.update_data()
```bash
String tableName = "ducument";
String searchId = "18301";
String columnName = "phone";
String updateData = "Mahfuz Salehin Moaz";

NextTable.update_data(tableName, searchId, columnName, updateData);
```

##  NextTable.delete_data()
```bash
String tableName = "ducument";
String searchId = "18301";
String columnName = "phone";

NextTable.delete_data(tableName, searchId, columnName);
```

##  NextTable.search_row_data()
```bash
String tableName = "ducument";
String searchId = "18301";

NextTable.search_row_data(tableName, searchId);
```
```bash
Output: Row data.
```

##  NextTable.update_row()
```bash
String tableName = "ducument";
String searchId = "18301";
String data = "18301|Al Moaz|016XXXXXXXX";

NextTable.update_row(tableName, searchId, data);
```

##  NextTable.delete_row()
```bash
String tableName = "ducument";
String searchId = "18301";

NextTable.delete_row(tableName, searchId);
```

##  NextTable.search_col_data()
```bash
String tableName = "ducument";
String columnName = "id";

NextTable.search_col_data(tableName, columnName);
```
```bash
Output: Column data.
```

##  NextTable.delete_col()
```bash
String tableName = "ducument";
String columnName = "phone";

NextTable.delete_col(tableName, columnName);
```

##  NextTable.table_to_doc()
```bash
String tableName = "ducument";
String columnName = "id";

NextTable.table_to_doc(tableName, columnName); 
```
