from ExtractTable import ExtractTable
et_sess = ExtractTable(api_key=’bNxrjf65b8AiqRc243d2WqNPoqn9l2q0uhdd67Jt’)        
print(et_sess.check_usage())        
table_data = et_sess.process_file(filepath=’Location_of_Image_with_Tables’, output_format="df")



