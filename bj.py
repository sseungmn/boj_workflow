import sys
from workflow import Workflow3, web
from bs4 import BeautifulSoup as bs

reload(sys)
sys.setdefaultencoding('utf-8')

def main(wf):
    query = wf.args[1]

    url = 'https://www.acmicpc.net/problem/{query}'.format(query=query)
    raw = web.get(url)
    html = raw.text

    parsing(url, html)

def parsing(url, html):
    soup = bs(html)
    header = soup.select('.page-header')[0]
    info = soup.select('#problem-info')[0]

    num=header.select('.printable')[0].text
    title=header.select('#problem_title')[0].text
    # lbl=[]
    # lbl_class=['.label-primary problem-label', '.label-purple problem-label']
    # for i in range(2):
        # if header.select(lbl_class[i]) is "":
            # lbl[i]={lbl_class[i]:'False'}
        # else:
            # lbl[i]={lbl_class[i]:'True'}

    total=info.select('tbody td:nth-child(3)')[0].text
    percent=info.select('tbody td:nth-child(6)')[0].text

    wf.add_item(
            title="{num} {title}".format(num=num, title=title),
            subtitle="Submitted:{t}, corrected:{p}".format(t=total, p=percent),
            valid=True,
            arg=url
            )

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
