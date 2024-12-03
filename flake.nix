{
  description = "`nix` shell for `aoc-2024`";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs =
    { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        overlays = [ (_: super: { python = super.python313; }) ];
        pkgs = import nixpkgs { inherit overlays system; };
      in
      {
        devShells.default = pkgs.mkShell {
          packages =
            (with pkgs; [
              python
              pyright
              ruff
              pylint
            ])
            ++ (with pkgs.pythonPackages; [
              numpy
              sympy
              more-itertools
              requests
              parse
            ])
            ++ (with pkgs; [
              (writeScriptBin "aoc" "${pkgs.python}/bin/python solve.py < input.txt")
              (writeScriptBin "aot" "${pkgs.python}/bin/python solve.py < sample.txt")
              (writeScriptBin "get" "${pkgs.python}/bin/python bin/get_input.py --day $1")
            ]);

          shellHook = with pkgs; ''
            ${python}/bin/python --version
          '';
        };
      }
    );
}
