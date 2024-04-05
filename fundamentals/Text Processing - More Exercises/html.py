title = input()
content = input()
result = (f'''
<h1>
    {title}
</h1>
<article>
    {content}
</article>''')
comment = input()

while comment != 'end of comments':
    result += ((f'\n<div>'
                f'\n    {comment}'
                f'\n</div>'))
    comment = input()
print(result)
