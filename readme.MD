# Import csv file
```
DROP TABLE public."Training";

CREATE TABLE public."Training"
(
    "PassengerId" integer NOT NULL,
    "Survived" char(1) NOT NULL,
    "Pclass" char(1),
    "Name" char(250),
    "Sex" char(10),
    "Age" numeric(5,2),
    "SibSp" integer,
    "Parch" integer,
    "Ticket" char(50),
    "Fare" numeric(10, 4),
    "Cabin" char(50),
    "Embarked" char(1),
    CONSTRAINT "Training_pkey" PRIMARY KEY ("PassengerId")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Training"
    OWNER to postgres;

COPY public."Training" FROM 'C:\Users\Daniemao\Documents\d3\Titanic\train.csv' DELIMITER ',' CSV HEADER;
```