{ lib, pkgs, ... }:

with lib;

let

  arduino = lowPrio pkgs.arduino;

in {
  commands = [
    { name = "arduino"; package = arduino; }
  ];
}
