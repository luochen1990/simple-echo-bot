{
  description = "A Python development environment with poetry";

  inputs = {
    nixpkgs.url = "nixpkgs";
  };

  outputs = { self, nixpkgs }:
  let
    supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
    eachSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f rec {
      inherit system;
      pkgs = import nixpkgs { inherit system; };
      python3 = pkgs.python3;
      py-version = pkgs.python3.version;
    });
  in
  {
    devShells = eachSystem ({pkgs, python3, ...}: rec {
      default = poetry;

      poetry = pkgs.mkShell {
        buildInputs = [
          python3
          pkgs.poetry
        ];

        shellHook = ''
          export PATH=$(poetry env info --path)/bin:$PATH
        '';
      };
    });

    apps = eachSystem ({system, pkgs, ...}: {
      default = {
        type = "app";
        program = "${pkgs.writeShellScript "bot" ''
          source ${self.devShells.${system}.default.shellHook}
          python src/bot.py
        ''}";
      };
    });

  };
}
