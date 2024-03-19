def print_pretty_window(term, title, subtitle, content):
    width = term.width
    height = term.height

    # Print top border
    print(term.bold('+') + term.bold('-' * (width - 2)) + term.bold('+'))

    # Print title
    title_padding = (width - len(title) - 4) // 2
    f = len(title) % 2
    print(term.bold('|') + ' ' * title_padding + term.bold(f' {title} ') + ' ' * (title_padding + f) + term.bold('|'))

    # Print middle border
    print(term.bold('|') + '-' * (width - 2) + term.bold('|'))

    # Print subtitle
    subtitle_lines = subtitle.split('\n')
    for line in subtitle_lines:
        padding = (width - len(line) - 2) // 2

        f = len(line) % 2      
        print(term.bold('|') + ' ' * padding + term.bold(line) + ' ' * (padding + f) + term.bold('|'))

    # Print content
    content_lines = content
    for line in content_lines:
        padding = (width - len(line) - 5)
        print(term.bold('|') + ' ' * 3 + line + ' ' * padding + term.bold('|'))

    # Print bottom border
    print(term.bold('+') + term.bold('-' * (width - 2)) + term.bold('+'))