FROM ruby:3.1-bullseye

# Install system dependencies
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev

# Install Jekyll and Bundler
RUN gem install jekyll bundler

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./

RUN bundle install

COPY . .

EXPOSE 3000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--port", "3000"]
