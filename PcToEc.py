import os
import re

dir1 ='D:\\sztc2\\2013-11-12 OracleToInformix\\oracle'
dir2 ='D:\\sztc2\\2013-11-12 OracleToInformix\\informix'


files = os.listdir(dir1)

for f in files:
    print f

    file1 = os.path.join(dir1,f)
    file_object = open(file1,'r')
    all_the_txt = file_object.read()

    file2 = all_the_txt.replace('struct sqlca sqlca;', '')

    file2 = file2.replace('EXEC SQL CONTEXT USE:m_pWorkThread->m_pvSqlCtx;','')

    file2 = file2.replace('sqlca.sqlcode', 'pSqlCa->sqlcode')

    file2 = file2.replace('sqlca.sqlerrm.sqlerrmc','pSqlCa->sqlerrm' )

    file2 = file2.replace('if(pSqlCa->sqlcode','struct sqlca_s * pSqlCa = ifx_sqlca();\n\tif(pSqlCa->sqlcode')

    file2 = file2.replace('else struct sqlca_s * pSqlCa = ifx_sqlca();\n\tif(pSqlCa->sqlcode',
                            'else if(pSqlCa->sqlcode' )

    file2 = file2.replace('DATA_NOT_FOUND','100' )

    file2 = file2.replace('if (100 == pSqlCa->sqlcode)', 
                            'pSqlCa = ifx_sqlca();\nif (DATA_NOT_FOUND == pSqlCa->sqlcode)')



    # file2 = file2.replace('&& pSqlCa->sqlerrd[2] > 0', '')
    # file2 = file2.replace('pSqlCa = ifx_sqlca();', '')
    # file2 = file2.replace('struct sqlca_s * pSqlCa = ifx_sqlca();', '')
    # file2 = file2.replace('EXEC SQL CLOSE C1;', 
    #     'struct sqlca sqlca;\n\tEXEC SQL CONTEXT USE:m_pWorkThread->m_pvSqlCtx;\n\tEXEC SQL CLOSE C1;')


    file_object2 = os.path.join(dir2,f)
    file_object3 = open(file_object2,'w')
    file_object3.write(file2)

    file_object.close()
    file_object3.close()