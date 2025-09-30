ALTER TABLE countries_rivers
ADD CONSTRAINT fk_countries_countries_rivers_country_code
FOREIGN KEY (country_code)
REFERENCES countries(country_code) ON UPDATE CASCADE;

ALTER TABLE countries_rivers
ADD CONSTRAINT fk_rivers_countries_rivers_river_id
FOREIGN KEY (river_id)
REFERENCES rivers(id) ON UPDATE CASCADE;