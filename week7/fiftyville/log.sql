-- Keep a log of any SQL queries you execute as you solve the mystery.
--GIVEN INFO
--DATE = 28 july
--Add = Chamberlin Street
.tables;
.schema crime_scene_reports;
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28;
SELECT Description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = "Humphrey Street";

--Two crimes, 1 Theft other littering with mention of bakrey in theft
--NEW info time 10:15 am, Key = 295
--there's a possibility of accomplice so first we will read the witness interview
.schema interviews;

SELECT name,transcript FROM interviews WHERE day = 28 AND month = 7 AND year = 2021;
--got a v cluttered output so checking again with bakery in query

SELECT name,transcript FROM interviews WHERE day = 28 AND month = 7 AND year = 2021 AND transcript LIKE "%bakery%";

--IMP INFO ATM money withdraw FROM Eugene Location Leggett Street, Planning on leaving fiftyville By raymond Hence airport check, Parking lot of bakery by RUTH,
--Starting with bakery logs combined with time frame we got

.schema people
.schema bakery_security_logs

SELECT name FROM people JOIN bakery_security_logs ON bakery_security_logs.license_plate = people,license_plate
WHERE year = 2021 AND day = 28 AND month = 7 AND hour = 10 AND minute > 14 AND minute < 26 AND activity = "exit";

-- Current SUSPECT LIST Vanessa,Bruce,Barry,Luca,Sofia,Iman,Diana,Kelsey

-- Now Following Eugene's interview
.schema atm_transactions
.schema bank_accounts
--We will join these in accordance with people table to get the name


SELECT name FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type LIKE "withdraw";

--Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor,Benista
--BY intersecting the ATM suspects with the bakery Suspect we get
--Bruce, Iman, Diana, Luca, 4 Common suspects


--There was a mention of phonecall of under a min with intentions to leave the city next day

.schema airports
.schema flights
.schema phone_calls
.schema passengers

SELECT name FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = (SELECT flights.id FROM flights
JOIN airports ON airports.city = ("Fiftyville")
WHERE year = 2021 AND month = 7 AND day = 29
ORDER BY hour,minute LIMIT 1);

-- Doris,Sofia,Bruce,Edward,Kelsey,Taylor,Kenny,Luca
-- Intersecting it with given suspect list (--Bruce, Iman, Diana, Luca)
-- Current suspect (Bruce , Luca)

-- as we know he called too so we will check caller logs now

SELECT name,receiver FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

--after intersection we can see that the "bruce" is our suspect so to check his accomplice we can use the provided number
-- "(375) 555-8161"

SELECT name FROM people WHERE phone_number = "(375) 555-8161";
--Now we know that Robin was the accomplice

SELECT city FROM airports
WHERE id = (SELECT destination_airport_id FROM flights
WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (
SELECT id FROM airports WHERE city = "Fiftyville")
ORDER BY hour, minute
LIMIT 1);

-- WITH the above query we can determine that the city in question is New York City

