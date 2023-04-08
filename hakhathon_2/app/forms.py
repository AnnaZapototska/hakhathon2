import flask_wtf
import wtforms


class MyForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Name", [wtforms.validators.Length(min=4, max=25)])
    password = wtforms.PasswordField("Password", [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")

