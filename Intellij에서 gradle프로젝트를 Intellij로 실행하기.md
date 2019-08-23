### Intellij에서 gradle프로젝트를 Gradle Daemon이 아닌 Intellij로 실행하기
* 문제 : Intellij 2019.2 버전에서 프로젝트를 Gradle로 구성할 경우 기본 gradle daemon으로 빌드 및 실행됨
* 조치 : File > Settings > Build, Execution, Deployment > Gradle 메뉴에서 `Build and run using: `과 `Run tests using: `을 'Intellij IDEA'로 변경해준다
