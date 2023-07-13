-- This script creates an index using the score & the first letters of the name 
CREATE INDEX idx_name_first_score ON names (name(1), score);
