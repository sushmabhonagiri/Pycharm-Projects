import pdftables_api

test1 = 'O:\\10. Workspace\\DI Jiras\\DI-696 Regional Daily Stats\\PDF\'s\\2018.pdf'
c = pdftables_api.Client('38apg7gvbye6')
c.xlsx(test1, 'output.xlsx')
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML

