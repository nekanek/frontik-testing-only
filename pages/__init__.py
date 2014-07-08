# coding=utf-8

import frontik.handler


class Page(frontik.handler.PageHandler):
    def get_page(self):
        self.json.put({
            'Hello': self.get_argument('param')
        })
