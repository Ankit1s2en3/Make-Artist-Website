from website import createApp

app = createApp()

if __name__ == '__main__':
    print(type(app))
    app.run(debug=True)