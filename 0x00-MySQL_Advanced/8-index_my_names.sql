-- This script creates an index using the first letters of the name column
CREATE INDEX idx_name_first ON names (name(1));
