from flask import Flask, render_template, redirect, request

from discord_oauth import DiscordOauth

app = Flask(__name__, static_url_path='/cdn')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/terms/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms/tos')
def tos():
    return render_template('tos.html')


@app.route('/invited')
def invited():
    return render_template('invited.html')


# Route for index page
# Provides user login capabilities
@app.route('/login', methods=['GET'])
def login():
    return redirect(DiscordOauth.login_url)


# Route for dashboard
@app.route('/dashboard', methods=['GET'])
def dashboard():
    code = request.args.get('code')
    access_token = DiscordOauth.get_access_token(code)
    print(access_token)
    if access_token:

        user_object = DiscordOauth.get_user(access_token)
        user_guild_object = DiscordOauth.get_user_current_guild(access_token)

        id, avatar, username, usertag = user_object.get('id'), user_object.get('avatar'), user_object.get('username'), \
                                        user_object.get('discriminator')

        return render_template('dashboard.html',
                               render_user_avatar=f'https://cdn.discordapp.com/avatars/{id}/{avatar}.png',
                               render_username=f'{username}#{usertag}', render_guild=user_guild_object)
    else:
        return redirect('login')
    
@app.errorhandler(404)
async def page_not_found_error(error):
    return render_template('404.html')


if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=8000)
    app.run(debug=False, host='0.0.0.0', port=1000)
    app.run(debug=False, host='192.168.1.73', port=8000)
