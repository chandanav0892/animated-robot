def printTohtml1(alist, htmlpage):
    html =  "<html>\n<head></head>\n<style>p { margin: 0 !important; }</style>\n<body>\n"
    
    
    for line in alist:
        html+= '<table><tr><th>Element</th><th>Occurance</th>'
        for ele,val in line:
            print(tup)
            html+= '<tr>'
            html+= '<td><p>%s</p></td>'%(ele)
            html+= '<td><p><a href="#" target="_blank">%s</p></td>'%(val)
            html+= '</tr>'
        html+= '</table>'
        print("--------")
    with open(htmlpage, 'w') as f:
        f.write(html + "\n</body>\n</html>")

alist = [[(0,123),(1,234),(3,23),(4,5)],
         [(0,123),(1,234),(3,23),(4,5)],
         [(0,123),(1,234),(3,23),(4,5)]]

printTohtml1(alist, 'files.html')
