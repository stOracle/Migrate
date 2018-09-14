require(tidyr)
require(dplyr)
require(rlang)
require(ggplot2)
require("jsonlite")
require("RCurl")
require(utf8)
require(chron)

setwd("C:/Users/srauner/git/twitter")

# open .csv files and bring them in as dataframes
file_path <- "tweets.csv"
file_path2 <- "users.csv"
dt <- read.csv(file_path, stringsAsFactors = FALSE)
du <- read.csv(file_path2, stringsAsFactors = FALSE)

# fix column names so columns match between tables 
dt <- dt %>% rename(screen_name = user_key)
du$screen_name <- tolower(du$screen_name)

# fix date columns
du <- du %>%
  separate(created_at, c("weekday", "month", "date", "hour", "minute", "sec", "del", "year")) 
dt <- dt %>%
  separate(created_str, c("date_created", "time_created"), sep = " ")

# reorganizes the columns and eliminates unneccessary ones
du <- du %>%
  select("user_id", "screen_name", "user_location", "followers_count", "statuses_count", 
         "user_time_zone", "lang", "month", "year", "friends_count")
dt <- dt %>%
  select("user_id", "screen_name", "tweet_id", "date_created")
gg 

du_final <- du %>% 
  filter(!is.na(user_id)) %>%
  filter(!is.na(screen_name)) %>%
  filter(!is.na(followers_count)) %>%
  filter(!is.na(statuses_count)) %>%
  filter(!is.na(month)) %>%
  filter(!is.na(year)) %>%
  filter(!is.na(friends_count))

dt_final <- dt %>%
  filter(!is.na(user_id)) %>%
  filter(!is.na(screen_name)) %>%
  filter(!is.na(tweet_id))

# write the new .csv files
write.csv(du_final, file = "users_clean.csv")
write.csv(dt_final, file = "tweets_clean.csv")

# Compiles list of users with tweets over 1000
high_posts <- dt %>% 
  select(c("user_id", "screen_name")) %>%
  filter(!is.na(user_key)) %>% 
  group_by(user_key) %>%
  filter(n() > 1000) %>% 
  count(user_key) %>%
  arrange(user_key) %>%
  rename(post_count = n)

#makes vector containing high posting usernames
prominent <-high_posts[["user_key"]]

#filters the user table to only keep users that are on prominent list
filt_user <- du %>% 
  filter(!is.na(screen_name)) %>%
  filter(tolower(screen_name) %in% prominent) %>%
  select("screen_name", "user_name", "followers_count", "user_time_zone", "lang", "friends_count") %>%
  arrange(screen_name)

du %>% count(user_time_zone)

filt_user
high_posts
test
test %>%
  count(user_key)
count(dt, user_id)

test <- dt %>% select(-"text") %>% filter(user_key == "kathiemrr") %>% mutate(count = n())


names(du)
str(df)
dplyr::glimpse(df)
