class blog:
    def __init__(self, 
                 user=None,
                 userPNG=None,
                 userFollowers=None,
                 userDescription='',
                 title=None,
                 subtitle=None,
                 post_date=None,
                 read_time=None,
                 reactions={
                     'claps': '0',
                     'Responds': '0'
                 },
                 tags=[],
                 data=''
        ) -> None:
        
        self.title = title
        self.user = user
        self.userPNG = userPNG
        self.userFollowers = userFollowers
        self.userDescription = userDescription
        self.subtitle = subtitle
        self.post_date = post_date
        self.read_time = read_time
        self.reactions = reactions
        self.tags = tags
        self.data = data
    
    @property
    def html(self): return self.data+self.getFooterHTML()
        
    def getHeadingHTML(self):
        html = f'<h1>{self.title}</h1>'
        if self.subtitle: html+=f'<h2 style="font-weight:300;">{self.subtitle}</h2>'
        html+=f'''<div class="heading-userData-container">
                <img alt="{self.user}" src="{self.userPNG}" width="44" height="44" loading="lazy">
                <div class="heading-userData">
                    <div>
                        <a href="#" id="userName">{self.user}</a> · <a href="#" class="follow">Follow</a>
                    </div>

                    <div style="font-size: 14px;">
                        {self.read_time} · {self.post_date}
                    </div>
                </div>
            </div>'''
        html+=f'''<div class="blog-reaction-div">
                <div class="blog-reaction">
                    <div>
                        <svg width="24" height="24" viewBox="0 0 24 24" aria-label="clap"><path fill-rule="evenodd" fill="currentColor" clip-rule="evenodd" d="M11.37.83L12 3.28l.63-2.45h-1.26zM13.92 3.95l1.52-2.1-1.18-.4-.34 2.5zM8.59 1.84l1.52 2.11-.34-2.5-1.18.4zM18.52 18.92a4.23 4.23 0 0 1-2.62 1.33l.41-.37c2.39-2.4 2.86-4.95 1.4-7.63l-.91-1.6-.8-1.67c-.25-.56-.19-.98.21-1.29a.7.7 0 0 1 .55-.13c.28.05.54.23.72.5l2.37 4.16c.97 1.62 1.14 4.23-1.33 6.7zm-11-.44l-4.15-4.15a.83.83 0 0 1 1.17-1.17l2.16 2.16a.37.37 0 0 0 .51-.52l-2.15-2.16L3.6 11.2a.83.83 0 0 1 1.17-1.17l3.43 3.44a.36.36 0 0 0 .52 0 .36.36 0 0 0 0-.52L5.29 9.51l-.97-.97a.83.83 0 0 1 0-1.16.84.84 0 0 1 1.17 0l.97.97 3.44 3.43a.36.36 0 0 0 .51 0 .37.37 0 0 0 0-.52L6.98 7.83a.82.82 0 0 1-.18-.9.82.82 0 0 1 .76-.51c.22 0 .43.09.58.24l5.8 5.79a.37.37 0 0 0 .58-.42L13.4 9.67c-.26-.56-.2-.98.2-1.29a.7.7 0 0 1 .55-.13c.28.05.55.23.73.5l2.2 3.86c1.3 2.38.87 4.59-1.29 6.75a4.65 4.65 0 0 1-4.19 1.37 7.73 7.73 0 0 1-4.07-2.25zm3.23-12.5l2.12 2.11c-.41.5-.47 1.17-.13 1.9l.22.46-3.52-3.53a.81.81 0 0 1-.1-.36c0-.23.09-.43.24-.59a.85.85 0 0 1 1.17 0zm7.36 1.7a1.86 1.86 0 0 0-1.23-.84 1.44 1.44 0 0 0-1.12.27c-.3.24-.5.55-.58.89-.25-.25-.57-.4-.91-.47-.28-.04-.56 0-.82.1l-2.18-2.18a1.56 1.56 0 0 0-2.2 0c-.2.2-.33.44-.4.7a1.56 1.56 0 0 0-2.63.75 1.6 1.6 0 0 0-2.23-.04 1.56 1.56 0 0 0 0 2.2c-.24.1-.5.24-.72.45a1.56 1.56 0 0 0 0 2.2l.52.52a1.56 1.56 0 0 0-.75 2.61L7 19a8.46 8.46 0 0 0 4.48 2.45 5.18 5.18 0 0 0 3.36-.5 4.89 4.89 0 0 0 4.2-1.51c2.75-2.77 2.54-5.74 1.43-7.59L18.1 7.68z"></path></svg>
                    </div>
                    <div>{self.reactions['claps']}</div>
                    <div style="margin-left: 16px;">
                        <svg width="24" height="24" viewBox="0 0 24 24" class="jp"><path d="M18 16.8a7.14 7.14 0 0 0 2.24-5.32c0-4.12-3.53-7.48-8.05-7.48C7.67 4 4 7.36 4 11.48c0 4.13 3.67 7.48 8.2 7.48a8.9 8.9 0 0 0 2.38-.32c.23.2.48.39.75.56 1.06.69 2.2 1.04 3.4 1.04.22 0 .4-.11.48-.29a.5.5 0 0 0-.04-.52 6.4 6.4 0 0 1-1.16-2.65v.02zm-3.12 1.06l-.06-.22-.32.1a8 8 0 0 1-2.3.33c-4.03 0-7.3-2.96-7.3-6.59S8.17 4.9 12.2 4.9c4 0 7.1 2.96 7.1 6.6 0 1.8-.6 3.47-2.02 4.72l-.2.16v.26l.02.3a6.74 6.74 0 0 0 .88 2.4 5.27 5.27 0 0 1-2.17-.86c-.28-.17-.72-.38-.94-.59l.01-.02z"></path></svg>
                    </div>
                    <div>{self.reactions['Responds']}</div>
                </div>
                <div class="blog-save-share">
                    <div>
                        <svg width="25" height="25" viewBox="0 0 25 25" fill="none" class="sg" aria-label="Add to list bookmark button"><path d="M18 2.5a.5.5 0 0 1 1 0V5h2.5a.5.5 0 0 1 0 1H19v2.5a.5.5 0 1 1-1 0V6h-2.5a.5.5 0 0 1 0-1H18V2.5zM7 7a1 1 0 0 1 1-1h3.5a.5.5 0 0 0 0-1H8a2 2 0 0 0-2 2v14a.5.5 0 0 0 .8.4l5.7-4.4 5.7 4.4a.5.5 0 0 0 .8-.4v-8.5a.5.5 0 0 0-1 0v7.48l-5.2-4a.5.5 0 0 0-.6 0l-5.2 4V7z" fill="currentColor"></path></svg>
                    </div>
                    <div>
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M3 12a9 9 0 1 1 18 0 9 9 0 0 1-18 0zm9-10a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm3.38 10.42l-4.6 3.06a.5.5 0 0 1-.78-.41V8.93c0-.4.45-.63.78-.41l4.6 3.06c.3.2.3.64 0 .84z" fill="currentColor"></path></svg>
                    </div>
                    <div>
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.22 4.93a.42.42 0 0 1-.12.13h.01a.45.45 0 0 1-.29.08.52.52 0 0 1-.3-.13L12.5 3v7.07a.5.5 0 0 1-.5.5.5.5 0 0 1-.5-.5V3.02l-2 2a.45.45 0 0 1-.57.04h-.02a.4.4 0 0 1-.16-.3.4.4 0 0 1 .1-.32l2.8-2.8a.5.5 0 0 1 .7 0l2.8 2.8a.42.42 0 0 1 .07.5zm-.1.14zm.88 2h1.5a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-11a2 2 0 0 1-2-2v-10a2 2 0 0 1 2-2H8a.5.5 0 0 1 .35.14c.1.1.15.22.15.35a.5.5 0 0 1-.15.35.5.5 0 0 1-.35.15H6.4c-.5 0-.9.4-.9.9v10.2a.9.9 0 0 0 .9.9h11.2c.5 0 .9-.4.9-.9V8.96c0-.5-.4-.9-.9-.9H16a.5.5 0 0 1 0-1z" fill="currentColor"></path></svg>
                    </div>
                </div>
            </div>'''
        return html
    def getFooterHTML(self):
        html = f'''<div class="tags">
                {''.join([f'<a href="#">{i}</a>' for i in self.tags])}
            </div>'''
        html += f'''<div class="blog-reaction-div" style="border:none">
                <div class="blog-reaction">
                    <div>
                        <svg width="24" height="24" viewBox="0 0 24 24" aria-label="clap"><path fill-rule="evenodd" fill="currentColor" clip-rule="evenodd" d="M11.37.83L12 3.28l.63-2.45h-1.26zM13.92 3.95l1.52-2.1-1.18-.4-.34 2.5zM8.59 1.84l1.52 2.11-.34-2.5-1.18.4zM18.52 18.92a4.23 4.23 0 0 1-2.62 1.33l.41-.37c2.39-2.4 2.86-4.95 1.4-7.63l-.91-1.6-.8-1.67c-.25-.56-.19-.98.21-1.29a.7.7 0 0 1 .55-.13c.28.05.54.23.72.5l2.37 4.16c.97 1.62 1.14 4.23-1.33 6.7zm-11-.44l-4.15-4.15a.83.83 0 0 1 1.17-1.17l2.16 2.16a.37.37 0 0 0 .51-.52l-2.15-2.16L3.6 11.2a.83.83 0 0 1 1.17-1.17l3.43 3.44a.36.36 0 0 0 .52 0 .36.36 0 0 0 0-.52L5.29 9.51l-.97-.97a.83.83 0 0 1 0-1.16.84.84 0 0 1 1.17 0l.97.97 3.44 3.43a.36.36 0 0 0 .51 0 .37.37 0 0 0 0-.52L6.98 7.83a.82.82 0 0 1-.18-.9.82.82 0 0 1 .76-.51c.22 0 .43.09.58.24l5.8 5.79a.37.37 0 0 0 .58-.42L13.4 9.67c-.26-.56-.2-.98.2-1.29a.7.7 0 0 1 .55-.13c.28.05.55.23.73.5l2.2 3.86c1.3 2.38.87 4.59-1.29 6.75a4.65 4.65 0 0 1-4.19 1.37 7.73 7.73 0 0 1-4.07-2.25zm3.23-12.5l2.12 2.11c-.41.5-.47 1.17-.13 1.9l.22.46-3.52-3.53a.81.81 0 0 1-.1-.36c0-.23.09-.43.24-.59a.85.85 0 0 1 1.17 0zm7.36 1.7a1.86 1.86 0 0 0-1.23-.84 1.44 1.44 0 0 0-1.12.27c-.3.24-.5.55-.58.89-.25-.25-.57-.4-.91-.47-.28-.04-.56 0-.82.1l-2.18-2.18a1.56 1.56 0 0 0-2.2 0c-.2.2-.33.44-.4.7a1.56 1.56 0 0 0-2.63.75 1.6 1.6 0 0 0-2.23-.04 1.56 1.56 0 0 0 0 2.2c-.24.1-.5.24-.72.45a1.56 1.56 0 0 0 0 2.2l.52.52a1.56 1.56 0 0 0-.75 2.61L7 19a8.46 8.46 0 0 0 4.48 2.45 5.18 5.18 0 0 0 3.36-.5 4.89 4.89 0 0 0 4.2-1.51c2.75-2.77 2.54-5.74 1.43-7.59L18.1 7.68z"></path></svg>
                    </div>
                    <div>{self.reactions['claps']}</div>
                    <div style="margin-left: 16px;">
                        <svg width="24" height="24" viewBox="0 0 24 24" class="jp"><path d="M18 16.8a7.14 7.14 0 0 0 2.24-5.32c0-4.12-3.53-7.48-8.05-7.48C7.67 4 4 7.36 4 11.48c0 4.13 3.67 7.48 8.2 7.48a8.9 8.9 0 0 0 2.38-.32c.23.2.48.39.75.56 1.06.69 2.2 1.04 3.4 1.04.22 0 .4-.11.48-.29a.5.5 0 0 0-.04-.52 6.4 6.4 0 0 1-1.16-2.65v.02zm-3.12 1.06l-.06-.22-.32.1a8 8 0 0 1-2.3.33c-4.03 0-7.3-2.96-7.3-6.59S8.17 4.9 12.2 4.9c4 0 7.1 2.96 7.1 6.6 0 1.8-.6 3.47-2.02 4.72l-.2.16v.26l.02.3a6.74 6.74 0 0 0 .88 2.4 5.27 5.27 0 0 1-2.17-.86c-.28-.17-.72-.38-.94-.59l.01-.02z"></path></svg>
                    </div>
                    <div>{self.reactions['Responds']}</div>
                </div>
                <div class="blog-save-share">
                    <div>
                        <svg width="25" height="25" viewBox="0 0 25 25" fill="none" class="sg" aria-label="Add to list bookmark button"><path d="M18 2.5a.5.5 0 0 1 1 0V5h2.5a.5.5 0 0 1 0 1H19v2.5a.5.5 0 1 1-1 0V6h-2.5a.5.5 0 0 1 0-1H18V2.5zM7 7a1 1 0 0 1 1-1h3.5a.5.5 0 0 0 0-1H8a2 2 0 0 0-2 2v14a.5.5 0 0 0 .8.4l5.7-4.4 5.7 4.4a.5.5 0 0 0 .8-.4v-8.5a.5.5 0 0 0-1 0v7.48l-5.2-4a.5.5 0 0 0-.6 0l-5.2 4V7z" fill="currentColor"></path></svg>
                    </div>
                    <div>
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.22 4.93a.42.42 0 0 1-.12.13h.01a.45.45 0 0 1-.29.08.52.52 0 0 1-.3-.13L12.5 3v7.07a.5.5 0 0 1-.5.5.5.5 0 0 1-.5-.5V3.02l-2 2a.45.45 0 0 1-.57.04h-.02a.4.4 0 0 1-.16-.3.4.4 0 0 1 .1-.32l2.8-2.8a.5.5 0 0 1 .7 0l2.8 2.8a.42.42 0 0 1 .07.5zm-.1.14zm.88 2h1.5a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-11a2 2 0 0 1-2-2v-10a2 2 0 0 1 2-2H8a.5.5 0 0 1 .35.14c.1.1.15.22.15.35a.5.5 0 0 1-.15.35.5.5 0 0 1-.35.15H6.4c-.5 0-.9.4-.9.9v10.2a.9.9 0 0 0 .9.9h11.2c.5 0 .9-.4.9-.9V8.96c0-.5-.4-.9-.9-.9H16a.5.5 0 0 1 0-1z" fill="currentColor"></path></svg>
                    </div>
                </div>
            </div>'''
        return html
    def getRootFooterHTML(self):
        html = f'''<div class="writer">
            <div class="writer-img">
                <img alt="{self.user}" src="{self.userPNG}" width="72" height="72" loading="lazy">
            </div>
            <div style="display: flex;flex-wrap: wrap;">
                <div style="padding-bottom: 1rem;">
                    <h2>Written by {self.user}</h2>
                    <div style="margin-bottom:8px;">
                        <a href="">{self.userFollowers} Followers</a>
                    </div>
                    <div>
                        {self.userDescription}
                    </div>
                </div>
                <div style="display: flex; flex-direction: row;gap:9px;flex-wrap: wrap;">
                    <button>
                        Follow
                    </button>
                    <button style="padding: 0px; height: 36px;">
                        <svg width="38" height="38" viewBox="0 0 38 38" fill="none" style="stroke: rgb(255, 255, 255);width: 36px;height: 36px;"><rect x="26.25" y="9.25" width="0.5" height="6.5" rx="0.25"></rect><rect x="29.75" y="12.25" width="0.5" height="6.5" rx="0.25" transform="rotate(90 29.75 12.25)"></rect><path d="M19.5 12.5h-7a1 1 0 0 0-1 1v11a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1v-5"></path><path d="M11.5 14.5L19 20l4-3"></path></svg>
                    </button>
                </div>
            </div>
        </div>'''
        return html
    
    def img(self, src, figCaption:str=None, fullWidth:bool=False) -> None: # full width not supported yet
        # if fullWidth:
        #     self.data+=f'''<div style="margin-bottom: 50%;">
        #                         <div style="position: absolute; left: 0;"></div>
        #                     </div>'''
        self.data+=f'<img alt=""  width="100%"  loading="eager" role="presentation" src="{src}">'
        if figCaption:
            self.data+=f'<figcaption>{figCaption}</figcaption>'    
    def h(self, title, h_i=2):
        self.data+=f'<h{h_i}>{title}</h{h_i}>'
    def p(self, data):
        self.data+=f'<p>{data}</p>'
    
    def add(self, html): self.data+=html
    
    def __repr__(self) -> str: return self.html

if __name__ == '__main__':
    pass
# b = blog(user='David Rose',
#          userPNG='https://miro.medium.com/v2/resize:fill:88:88/1*qt83NUQLLkTSKMQ-iuMfwg.jpeg',
#          title='Fine-tuning LLMs: Practical Techniques and Helpful Tips',
#          post_date='Sep 28',
#          read_time='18 min',
#          reactions={
#              'claps': '51',
#              'Responds': '1'
#          },
#          tags=['Machine Learning', 'Deep Learning', 'Data Science', 'Artificial Intelligence', 'Python'])

# b.p('When designing and training an LLM for the task of text generation, there are two general paradigms to focus on. Pre-training, which is mostly focused on structure, language, and knowledge. While fine-tuning helps to guide style and presentation of the outputs generated.')
# b.img('https://miro.medium.com/v2/resize:fit:1050/1*86LtcB0OsJDD425G0Lt5OQ.png')
# b.h('When fine-tuning is useful', 1)
# b.h('Domain specific tasks')
# b.p('Tuning allows businesses to tailor the model to their specific needs and industry-specific terminology, leading to improved accuracy and relevance. For example, a customer service chatbot would want to be kind, helpful, and understanding, in which case you could help fine-tune it on a representative dataset in that style.')
# b.p('Also helping use LLMs for APIs or code outputs. You can use a code-based dataset to help the model learn to output correct language syntax rather than natural language responses, helping it to better interact with other computer systems.')
# b.h('Security and Privacy')
# b.p('Businesses can ensure their proprietary or sensitive data never leaves their controlled environment. This is particularly crucial for industries where data privacy regulations are stringent. Moreover, a custom tuned LLM can be trained to align more closely with a company’s brand voice and communication style, ensuring consistency across digital interactions. In contrast, a generic model might not always reflect the nuances and specifics of individual business needs or industry standards. This could be important if you are working in a regulated domain such as health or legal fields.')

# from readMarkdown import extract_markdown
# with open('b1.md', 'r', encoding='utf-8') as file:
#     markdown_text = file.read()
# b.add(extract_markdown(markdown_text))