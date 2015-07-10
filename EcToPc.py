import os

dir1 ='D:/9-4/ec'
dir2 ='D:/9-4/pc'

files = os.listdir(dir1)

for f in files:
    print f

    file1 = os.path.join(dir1,f)
    file_object = open(file1,'r')
    all_the_txt = file_object.read()

    file2 = all_the_txt.replace('EXEC SQL BEGIN DECLARE SECTION;', 
        'struct sqlca sqlca;\n\tEXEC SQL CONTEXT USE:m_pWorkThread->m_pvSqlCtx;\n\n\tEXEC SQL BEGIN DECLARE SECTION;')
    file2 = file2.replace('struct sqlca_s * pSqlCa = ifx_sqlca();','')
    file2 = file2.replace('pSqlCa->sqlcode', 'sqlca.sqlcode')
    file2 = file2.replace('pSqlCa->sqlerrm', 'sqlca.sqlerrm.sqlerrmc')
    file2 = file2.replace('100', 'DATA_NOT_FOUND')
    file2 = file2.replace('1403', 'DATA_NOT_FOUND')
    file2 = file2.replace('&& pSqlCa->sqlerrd[2] > 0', '')
    file2 = file2.replace('pSqlCa = ifx_sqlca();', '')
    file2 = file2.replace('struct sqlca_s * pSqlCa = ifx_sqlca();', '')
    file2 = file2.replace('EXEC SQL CLOSE C1;', 
        'struct sqlca sqlca;\n\tEXEC SQL CONTEXT USE:m_pWorkThread->m_pvSqlCtx;\n\tEXEC SQL CLOSE C1;')
    

    file_object2 = os.path.join(dir2,f)
    file_object3 = open(file_object2,'w')
    file_object3.write(file2)
    
    file_object.close()
    file_object3.close()