{
  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";

    nixpkgs.url = "github:NixOS/nixpkgs/release-25.05";
  };

  outputs = inputs @ { flake-parts, nixpkgs, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" ];

      perSystem = { config, pkgs, ... }: {
        packages = rec {
          python = pkgs.python313.withPackages (pyPkgs: with pyPkgs; [
            unittest-xml-reporting
          ]);
          default = python;
        };
      };
    };
}

