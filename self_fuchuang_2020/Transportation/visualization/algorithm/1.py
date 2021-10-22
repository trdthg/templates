routes = {
    '1号线': ['Sta65', 'Sta49', 'Sta149', 'Sta74', 'Sta128', 'Sta34', 'Sta106', 'Sta110', 'Sta97', 'Sta80', 'Sta89', 'Sta64', 'Sta150', 'Sta154', 'Sta107', 'Sta83', 'Sta108', 'sta47','Sta159', 'Sta1'], 
    '2号线': ['Sta63','Sta129', 'Sta9', 'Sta163', 'Sta53', 'Sta79', 'Sta18', 'Sta47', 'Sta123', 'Sta127', 'Sta81', 'Sta27', 'Sta48', 'Sta151', 'Sta68', 'Sta52', 'Sta76', 'Sta57', 'Sta71', 'Sta139', 'Sta105', 'Sta51', 'Sta24'], 
    '3号线': ['Sta143', 'Sta156', 'Sta61', 'Sta50', 'Sta119', 'Sta66', 'Sta12', 'Sta161', 'Sta21', 'Sta133', 'Sta22', 'Sta138', 'Sta41', 'Sta30', 'Sta67', 'Sta144', 'Sta29', 'Sta126','Sta115', 'Sta40', 'Sta131', 'Sta39', 'Sta100','Sta135', 'Sta167', 'Sta113', 'Sta141', 'Sta142', 'Sta158', 'Sta44', 'Sta117', 'Sta147', 'Sta42', 'Sta35','Sta87' 'Sta109', 'Sta33', 'Sta112', 'Sta153', 'Sta125', 'Sta121', 'Sta11'], 
    '10号线': ['Sta157', 'Sta114', 'Sta168', 'Sta135', 'Sta134', 'Sta85', 'Sta2', 'Sta4', 'Sta103', 'Sta145', 'Sta88', 'Sta87', 'Sta94', 'Sta160', 'Sta7', 'Sta6', 'Sta8', 'Sta75', 'Sta102'], 
    '4号线': ['Sta90','Sta84', 'Sta59', 'Sta19', 'Sta62', 'Sta165', 'Sta38', 'Sta58'], 
    '5号线': ['Sta43', 'Sta10', 'Sta96', 'Sta132', 'Sta37', 'Sta16', 'Sta69', 'Sta54', 'Sta56'], 
    '11号线': ['Sta45','Sta75', 'Sta152', 'Sta164', 'Sta82', 'Sta111', 'Sta140', 'Sta13', 'Sta70', 'Sta55', 'Sta20', 'Sta23', 'Sta56', 'Sta118', 'Sta115', 'Sta162','Sta114', 'Sta15', 'Sta86', 'Sta46', 'Sta3','Sta63',  'Sta25', 'Sta146', 'Sta130', 'Sta120'], 
    '11号线_': ['Sta77', 'Sta122', 'Sta36', 'Sta28', 'Sta124', 'Sta166', 'Sta99', 'Sta140'],
    '12号线': ['Sta136','Sta89', 'Sta137', 'Sta101', 'Sta31', 'Sta17','Sta23', 'Sta26', 'Sta90','Sta134', 'Sta95','Sta15', 'Sta72', 'Sta93','Sta3', 'Sta92', 'Sta116', 'Sta32','Sta41', 'Sta91','Sta127', 'Sta60', 'Sta148', 'Sta73']
}
datadict = {
    '1号线': ['Sta65', '3',  'Sta49', '4',  'Sta149', '4', 'Sta74', '4',  'Sta128', '7', 'Sta34', '3', 'Sta106', '4', 'Sta110', '4', 'Sta97', '3', 'Sta80', '3', 'Sta89', '2', 'Sta64', '3', 'Sta150', '4', 'Sta154', '3', 'Sta107', '3', 'Sta83', '3', 'Sta108', '5', 'Sta159', '5', 'Sta1', '30'], 
    '2号线': ['Sta129', '3', 'Sta9', '3',   'Sta163', '3', 'Sta53', '3',  'Sta78', '5', 'Sta79', '3', 'Sta18', '4', 'Sta47', '3', 'Sta123', '3', 'Sta127', '3', 'Sta81', '3', 'Sta27', '3', 'Sta48', '4', 'Sta151', '5', 'Sta68', '3', 'Sta52', '3', 'Sta76', '4', 'Sta57', '6', 'Sta71', '5', 'Sta139', '7', 'Sta105', '6', 'Sta51', '10', 'Sta24', '55'], 
    '3号线': ['Sta143', '4', 'Sta156', '4', 'Sta61', '3',  'Sta50', '4',  'Sta119', '6', 'Sta66', '4', 'Sta12', '4', 'Sta161', '4', 'Sta21', '4', 'Sta133', '3', 'Sta22', '3', 'Sta138', '4', 'Sta41', '4', 'Sta30', '2', 'Sta67', '3', 'Sta144', '9', 'Sta29', '2', 'Sta126', '6', 'Sta40', '3', 'Sta131', '3', 'Sta39', '3', 'Sta100', '4', 'Sta167', '4', 'Sta113', '3', 'Sta141', '4', 'Sta142', '4', 'Sta158', '3', 'Sta44', '3', 'Sta117', '4', 'Sta147', '5', 'Sta42', '3', 'Sta35', '4', 'Sta109', '5', 'Sta33', '4', 'Sta112', '4', 'Sta153', '5', 'Sta125', '3', 'Sta121', '4', 'Sta11', '123'], 
    '10号线':['Sta157', '5', 'Sta114', '3', 'Sta168', '5', 'Sta135', '4', 'Sta134', '4', 'Sta85', '5', 'Sta2', '5', 'Sta4', '5', 'Sta103', '5', 'Sta145', '7', 'Sta88', '3', 'Sta87', '4', 'Sta94', '4', 'Sta160', '4', 'Sta7', '5', 'Sta6', '5', 'Sta8', '5', 'Sta75', '5', 'Sta102', '62'], 
    '4号线': ['Sta84', '8',  'Sta59', '5',  'Sta19', '6',  'Sta62', '8',  'Sta165', '9', 'Sta38', '8', 'Sta58', '24'], 
    '5号线': ['Sta43', '6',  'Sta10', '4',  'Sta96', '4',  'Sta132', '4', 'Sta37', '3', 'Sta16', '4', 'Sta69', '10', 'Sta54', '26'], 
    '11号线':['Sta77', '4',  'Sta122', '5', 'Sta36', '16', 'Sta28', '3',  'Sta124', '7', 'Sta166', '3', 'Sta99', '30', 'Sta45', '10', 'Sta152', '5', 'Sta164', '5', 'Sta82', '4', 'Sta111', '4', 'Sta140', '6', 'Sta13', '4', 'Sta70', '3', 'Sta55', '4', 'Sta20', '3', 'Sta23', '3', 'Sta56', '4', 'Sta118', '4', 'Sta115', '3', 'Sta162', '6', 'Sta15', '4', 'Sta86', '3', 'Sta46', '3', 'Sta63', '3', 'Sta3', '7', 'Sta25', '4', 'Sta146', '3', 'Sta130', '3', 'Sta120', '59'], 
    '12号线':['Sta136', '7', 'Sta137', '4', 'Sta101', '5', 'Sta31', '3',  'Sta17', '5', 'Sta26', '3', 'Sta90', '9', 'Sta95', '7', 'Sta72', '4', 'Sta93', '8', 'Sta92', '9', 'Sta116', '6', 'Sta32', '4', 'Sta91', '8', 'Sta60', '3', 'Sta148', '3', 'Sta73', '72'],
}
changestations = {
    'Sta89': ['1号线','12号线'],
    'Sta47': ['1号线', '2号线'],

    'Sta63': ['11号线', '2号线'],

    'Sta41': ['3号线', '12号线'],
    'Sta115':['3号线', '11号线'],
    'Sta135':['3号线', '10号线'],
    'Sta87': ['3号线', '11号线'],

    'Sta114': ['10号线','11号线'],
    'Sta134': ['10号线','12号线'],
    'Sta87': ['3号线','10号线'],

    'Sta90': ['12号线','4号线'],

    'Sta56': ['11号线','5号线'],

    'Sta140':['11号线', '11号线_'],

    'Sta23': ['11号线','12号线'],

    'Sta15': ['11号线','12号线'],
    'Sta3': ['11号线','12号线'],
}

# 最少站到达目的地
# Sta89 -> Sta3
    
