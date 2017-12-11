install.packages('babynames')
install.packages('RPostgreSQL')

library(babynames)
library(RPostgreSQL)
library(dplyr)

df <- data.frame(babynames)


# create a connection
# loads the PostgreSQL driver
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "Website_Data",
                 host = "localhost", port = 5432,
                 user = "postgres", password = 'mys3326999')


# check for the cartable assuming babynames table has been created in PostgreSQL
dbExistsTable(con, "babynames")
# TRUE



# append dataframe to babynames table which has already been created in PostgreSQL
#dbWriteTable(con, "babynames", 
#             value = df, append = TRUE, row.names = FALSE)

if(dbExistsTable(con, "babynames2")){
  dbRemoveTable(con, "babynames2")
  dbWriteTable(con, "babynames2", , row.names = FALSE, value = df)
}

# query the data from postgreSQL 
df_postgres <- dbGetQuery(con, "SELECT * from babynames2")

str(df_postgres2)
str(df)


summary(df_postgres)
df %>% group_by(sex) %>% 
  summarise(n())

df_postgres %>% group_by(sex) %>% 
  summarise(n())
# compares the two data.frames
identical(df, df_postgres)
identical(df, df_postgres2)
# TRUE
