def main():
    from ssh_manager import create_app
    bolinette = create_app()
    bolinette.exec_cmd_args()

if __name__ == '__main__':
    main()
