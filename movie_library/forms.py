from typing import Any, TypeAlias

from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    StringField,
    SubmitField,
    TextAreaField,
    URLField,
    PasswordField,
)
from wtforms.validators import InputRequired, NumberRange, Email, Length, EqualTo

stf: TypeAlias = StringField


class MovieForm(FlaskForm):
    title: stf = StringField("Title", validators=[InputRequired()])
    director: stf = StringField("Director", validators=[InputRequired()])
    
    year: IntegerField = IntegerField(
        "Year", validators=[
            InputRequired(),
            NumberRange(
                min=1878,
                message="Please enter a year in the format YYYY."
            )
        ]
    )
    
    submit: SubmitField = SubmitField("Add Movie")


class StringListField(TextAreaField):
    def _value(self) -> str:
        if self.data:
            return "\n".join(self.data)
        else:
            return ""
        
    def process_formdata(self, valuelist: list[Any]) -> Any:
        if valuelist and valuelist[0]:
            self.data: list[Any] = [
                line.strip() for line in valuelist[0].split("\n")
            ]
        else:
            self.data: list[Any] = []


class ExtendedMovieForm(MovieForm):
    cast: stf = StringListField("Cast")
    series: stf = StringListField("Series")
    tags: stf = StringListField("Tags")
    description: TextAreaField = TextAreaField("Description")
    video_link: URLField = URLField("Video link")
    
    submit: SubmitField = SubmitField("Submit")


class RegisterForm(FlaskForm):
    email: stf = StringField("Email", validators=[InputRequired(), Email()])
    password: PasswordField = PasswordField(
        "Password",
        validators=[
            Length(
                min=4,
                max=20,
                message="Your password must be between \
                    4 and 20 characters long."
            )
        ]
    )    
    confirm_password: PasswordField = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(), EqualTo(
                "password",
                message="This password did not match \
                    the one in the password field."
            )
        ]
    )
    submit: SubmitField = SubmitField("Register")


class LoginForm(FlaskForm):
    email: StringField = StringField(
        "Email",
        validators=[InputRequired(), Email()]
    )
    password: PasswordField = PasswordField(
        "Password",
        validators=[InputRequired()]
    )
    submit: SubmitField = SubmitField("Login")
