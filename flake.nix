{
  inputs = {
    nixpkgs.url = "nixpkgs";
    devhsell = {
      url = "github:numtide/devshell";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { devshell, nixpkgs, ... } @ inputs: let
    systems = [ "x86_64-linux" ];
    mkOutputs = system: let
      nixpkgs' = inputs.nixpkgs;
      nixpkgs = let
        nixpkgs = import nixpkgs' {
          inherit system;
          overlays = [ devshell.overlay ];
        };
      in nixpkgs'.lib.recursiveUpdate nixpkgs' nixpkgs;
    in {
      devShell.${system} = nixpkgs.devshell.fromTOML ./devshell.toml;
    };
  in with nixpkgs.lib; foldl' recursiveUpdate { } (map mkOutputs systems);
}
