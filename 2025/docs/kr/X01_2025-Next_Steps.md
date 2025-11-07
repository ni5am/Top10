<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

# 다음 단계 (Next Steps)

설계상 OWASP Top 10은 본질적으로 10개의 가장 중요한 위험으로 제한됩니다. 모든 OWASP Top 10에는 포함을 위해 길게 고려되었지만 결국 포함되지 않은 "경계선" 위험이 있습니다. 다른 위험이 더 널리 퍼져 있고 영향이 컸습니다.

다음 두 가지 문제는 성숙한 appsec 프로그램을 향해 노력하는 조직, 보안 컨설팅 회사, 또는 제품의 커버리지를 확장하려는 도구 벤더에게 식별하고 수정할 가치가 있습니다.


## X01:2025 애플리케이션 복원력 부족 (Lack of Application Resilience)

### 배경 (Background). 

이것은 2021년의 서비스 거부(Denial of Service)의 이름 변경입니다. 그것은 근본 원인보다 증상을 설명했기 때문에 이름이 변경되었습니다. 이 카테고리는 복원력 문제와 관련된 약점을 설명하는 CWE에 초점을 맞춥니다. 이 카테고리의 점수는 A10:2025-예외 조건 처리 오류(Mishandling of Exceptional Conditions)와 매우 가까웠습니다. 관련 CWE에는 다음이 포함됩니다: *CWE-400 제어되지 않은 리소스 소비 (Uncontrolled Resource Consumption), CWE-409 고도로 압축된 데이터의 부적절한 처리 (데이터 증폭, Improper Handling of Highly Compressed Data (Data Amplification)), CWE-674 제어되지 않은 재귀 (Uncontrolled Recursion)*, *CWE-835 도달할 수 없는 종료 조건이 있는 루프 ('무한 루프', Loop with Unreachable Exit Condition ('Infinite Loop')).*


### 점수 표 (Score table).


<table>
  <tr>
   <td>매핑된 CWE (CWEs Mapped) 
   </td>
   <td>최대 발생률 (Max Incidence Rate)
   </td>
   <td>평균 발생률 (Avg Incidence Rate)
   </td>
   <td>최대 커버리지 (Max Coverage)
   </td>
   <td>평균 커버리지 (Avg Coverage)
   </td>
   <td>평균 가중 악용 (Avg Weighted Exploit)
   </td>
   <td>평균 가중 영향 (Avg Weighted Impact)
   </td>
   <td>총 발생 횟수 (Total Occurrences)
   </td>
   <td>총 CVE (Total CVEs)
   </td>
  </tr>
  <tr>
   <td>16
   </td>
   <td>20.05%
   </td>
   <td>4.55%
   </td>
   <td>86.01%
   </td>
   <td>41.47%
   </td>
   <td>7.92
   </td>
   <td>3.49
   </td>
   <td>865,066
   </td>
   <td>4,423
   </td>
  </tr>
</table>



### 설명 (Description). 

이 카테고리는 애플리케이션이 스트레스, 실패 및 엣지 케이스에 응답하는 방식에서 실패로부터 복구할 수 없는 체계적 약점을 나타냅니다. 애플리케이션이 예상치 못한 조건, 리소스 제약 및 기타 불리한 이벤트로부터 우아하게 처리, 견디거나 복구하지 않을 때 가용성 문제(가장 일반적으로)뿐만 아니라 데이터 손상, 민감한 데이터 공개, 연쇄 실패 및/또는 보안 제어 우회로 쉽게 이어질 수 있습니다.

또한 [X02:2025 메모리 관리 실패 (Memory Management Failures)](#x022025-memory-management-failures)는 애플리케이션 또는 전체 시스템의 실패로 이어질 수 있습니다.

### 예방 방법 (How to prevent) 

이 유형의 취약점을 방지하려면 시스템의 실패와 복구를 위해 설계해야 합니다.

* 제한, 할당량 및 장애 조치 기능을 추가하세요. 특히 가장 리소스를 많이 소비하는 작업에 특별한 주의를 기울이세요.
* 리소스 집약적인 페이지를 식별하고 미리 계획하세요: 특히 알려지지 않았거나 신뢰할 수 없는 사용자에게 많은 리소스(예: CPU, 메모리)가 필요한 불필요한 '가젯' 및 기능을 노출하지 않는 공격 표면 감소
* 허용 목록 및 크기 제한으로 엄격한 입력 검증을 수행한 다음 철저히 테스트하세요.
* 응답 크기를 제한하고 원시 응답을 클라이언트에게 다시 보내지 마세요(서버 측에서 처리).
* 기본적으로 안전/닫힘(절대 열림 아님), 기본적으로 거부하고 오류가 있으면 롤백하세요.
* 요청 스레드에서 차단 동기 호출을 피하세요(비동기/논블로킹 사용, 타임아웃, 동시성 제한 등).
* 오류 처리 기능을 신중하게 테스트하세요.
* 서킷 브레이커, 벌크헤드, 재시도 로직 및 우아한 저하와 같은 복원력 패턴을 구현하세요.
* 성능 및 부하 테스트를 수행하세요. 위험 감수 성향이 있다면 카오스 엔지니어링을 추가하세요.
* 합리적이고 감당할 수 있는 곳에서 중복을 구현하고 아키텍처하세요.
* 모니터링, 관찰 가능성 및 알림을 구현하세요.
* RFC 2267에 따라 잘못된 발신자 주소를 필터링하세요.
* 지문, IP 또는 동적으로 행동으로 알려진 봇넷을 차단하세요.
* 작업 증명(Proof-of-Work): 일반 사용자에게 큰 영향을 주지 않지만 많은 양의 요청을 보내려는 봇에 영향을 주는 *공격자* 측에서 리소스를 소비하는 작업을 시작하세요. 시스템의 일반 부하가 증가하면 작업 증명을 더 어렵게 만드세요. 특히 덜 신뢰할 수 있거나 봇으로 보이는 시스템의 경우 그렇습니다.
* 비활성 및 최종 타임아웃을 기반으로 서버 측 세션 시간을 제한하세요.
* 세션 바인딩 정보 저장을 제한하세요.


### 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1:** 공격자가 시스템 내에서 실패를 트리거하기 위해 의도적으로 애플리케이션 리소스를 소비하여 서비스 거부를 초래합니다. 이것은 메모리 고갈, 디스크 공간 채우기, CPU 포화 또는 끝없는 연결 열기일 수 있습니다.

**시나리오 #2:** 애플리케이션 비즈니스 로직을 깨는 제작된 응답으로 이어지는 입력 퍼징.

**시나리오 #3:** 공격자가 애플리케이션의 종속성에 초점을 맞추어 API나 기타 외부 서비스를 다운시키고 애플리케이션이 계속할 수 없게 됩니다.


### 참고 자료 (References). 

* [OWASP 치트 시트: 서비스 거부 (OWASP Cheat Sheet: Denial of Service)](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html)
* [OWASP MASVS‑RESILIENCE](https://mas.owasp.org/MASVS/11-MASVS-RESILIENCE/)
* [ASP.NET Core 모범 사례 (Microsoft) (ASP.NET Core Best Practices (Microsoft))](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices?view=aspnetcore-9.0)
* [마이크로서비스의 복원력: 벌크헤드 대 서킷 브레이커 (Parser) (Resilience in Microservices: Bulkhead vs Circuit Breaker (Parser))](https://medium.com/@parserdigital/resilience-in-microservices-bulkhead-vs-circuit-breaker-54364c1f9d53)
* [벌크헤드 패턴 (Geeks for Geeks) (Bulkhead Pattern (Geeks for Geeks))](https://www.geeksforgeeks.org/system-design/bulkhead-pattern/)
* [NIST 사이버보안 프레임워크 (CSF) (NIST Cybersecurity Framework (CSF))](https://www.nist.gov/cyberframework)
* [차단 호출 피하기: Java에서 비동기로 이동 (Devlane) (Avoid Blocking Calls: Go Async in Java (Devlane))](https://www.devlane.com/blog/avoid-blocking-calls-go-async-in-java)

## 매핑된 CWE 목록 (List of Mapped CWEs)
* [CWE-73  파일 이름 또는 경로의 외부 제어 (External Control of File Name or Path)](https://cwe.mitre.org/data/definitions/73.html)
* [CWE-183 허용된 입력의 허용적 목록 (Permissive List of Allowed Inputs)](https://cwe.mitre.org/data/definitions/183.html)
* [CWE-256 암호의 평문 저장 (Plaintext Storage of a Password)](https://cwe.mitre.org/data/definitions/256.html)
* [CWE-266 잘못된 권한 할당 (Incorrect Privilege Assignment)](https://cwe.mitre.org/data/definitions/266.html)
* [CWE-269 부적절한 권한 관리 (Improper Privilege Management)](https://cwe.mitre.org/data/definitions/269.html)
* [CWE-286 잘못된 사용자 관리 (Incorrect User Management)](https://cwe.mitre.org/data/definitions/286.html)
* [CWE-311 민감한 데이터의 암호화 누락 (Missing Encryption of Sensitive Data)](https://cwe.mitre.org/data/definitions/311.html)
* [CWE-312 민감한 정보의 평문 저장 (Cleartext Storage of Sensitive Information)](https://cwe.mitre.org/data/definitions/312.html)
* [CWE-313 파일 또는 디스크의 평문 저장 (Cleartext Storage in a File or on Disk)](https://cwe.mitre.org/data/definitions/313.html)
* [CWE-316 메모리의 민감한 정보 평문 저장 (Cleartext Storage of Sensitive Information in Memory)](https://cwe.mitre.org/data/definitions/316.html)
* [CWE-362 부적절한 동기화를 사용한 공유 리소스의 동시 실행 ('경쟁 조건', Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition'))](https://cwe.mitre.org/data/definitions/362.html)
* [CWE-382 J2EE 나쁜 관행: System.exit() 사용 (J2EE Bad Practices: Use of System.exit())](https://cwe.mitre.org/data/definitions/382.html)
* [CWE-419 보호되지 않은 기본 채널 (Unprotected Primary Channel)](https://cwe.mitre.org/data/definitions/419.html)
* [CWE-434 위험한 유형의 파일 무제한 업로드 (Unrestricted Upload of File with Dangerous Type)](https://cwe.mitre.org/data/definitions/434.html)
* [CWE-436 해석 충돌 (Interpretation Conflict)](https://cwe.mitre.org/data/definitions/436.html)
* [CWE-444 HTTP 요청의 일관성 없는 해석 ('HTTP 요청/응답 스머글링', Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling'))](https://cwe.mitre.org/data/definitions/444.html)
* [CWE-451 사용자 인터페이스(UI)의 중요한 정보 잘못된 표현 (User Interface (UI) Misrepresentation of Critical Information)](https://cwe.mitre.org/data/definitions/451.html)
* [CWE-454 신뢰할 수 있는 변수 또는 데이터 저장소의 외부 초기화 (External Initialization of Trusted Variables or Data Stores)](https://cwe.mitre.org/data/definitions/454.html)
* [CWE-472 가정된 불변 웹 매개변수의 외부 제어 (External Control of Assumed-Immutable Web Parameter)](https://cwe.mitre.org/data/definitions/472.html)
* [CWE-501 신뢰 경계 위반 (Trust Boundary Violation)](https://cwe.mitre.org/data/definitions/501.html)
* [CWE-522 불충분하게 보호된 자격 증명 (Insufficiently Protected Credentials)](https://cwe.mitre.org/data/definitions/522.html)
* [CWE-525 민감한 정보를 포함하는 웹 브라우저 캐시 사용 (Use of Web Browser Cache Containing Sensitive Information)](https://cwe.mitre.org/data/definitions/20.html)
* [CWE-539 민감한 정보를 포함하는 영구 쿠키 사용 (Use of Persistent Cookies Containing Sensitive Information)](https://cwe.mitre.org/data/definitions/525.html)
* [CWE-598 민감한 쿼리 문자열이 있는 GET 요청 메서드 사용 (Use of GET Request Method With Sensitive Query Strings)](https://cwe.mitre.org/data/definitions/598.html)
* [CWE-602 서버 측 보안의 클라이언트 측 강제 (Client-Side Enforcement of Server-Side Security)](https://cwe.mitre.org/data/definitions/602.html)
* [CWE-628 잘못 지정된 인수가 있는 함수 호출 (Function Call with Incorrectly Specified Arguments)](https://cwe.mitre.org/data/definitions/628.html)
* [CWE-642 중요한 상태 데이터의 외부 제어 (External Control of Critical State Data)](https://cwe.mitre.org/data/definitions/642.html)
* [CWE-646 외부에서 제공된 파일의 파일 이름 또는 확장자에 대한 의존 (Reliance on File Name or Extension of Externally-Supplied File)](https://cwe.mitre.org/data/definitions/646.html)
* [CWE-653 부적절한 격리 또는 구획화 (Improper Isolation or Compartmentalization)](https://cwe.mitre.org/data/definitions/653.html)
* [CWE-656 모호성을 통한 보안에 대한 의존 (Reliance on Security Through Obscurity)](https://cwe.mitre.org/data/definitions/656.html)
* [CWE-657 안전한 설계 원칙 위반 (Violation of Secure Design Principles)](https://cwe.mitre.org/data/definitions/657.html)
* [CWE-676 잠재적으로 위험한 함수 사용 (Use of Potentially Dangerous Function)](https://cwe.mitre.org/data/definitions/676.html)
* [CWE-693 보호 메커니즘 실패 (Protection Mechanism Failure)](https://cwe.mitre.org/data/definitions/693.html)
* [CWE-799 상호작용 빈도의 부적절한 제어 (Improper Control of Interaction Frequency)](https://cwe.mitre.org/data/definitions/799.html)
* [CWE-807 보안 결정에서 신뢰할 수 없는 입력에 대한 의존 (Reliance on Untrusted Inputs in a Security Decision)](https://cwe.mitre.org/data/definitions/807.html)
* [CWE-841 행동 워크플로우의 부적절한 강제 (Improper Enforcement of Behavioral Workflow)](https://cwe.mitre.org/data/definitions/841.html)
* [CWE-1021 렌더링된 UI 레이어 또는 프레임의 부적절한 제한 (Improper Restriction of Rendered UI Layers or Frames)](https://cwe.mitre.org/data/definitions/1021.html)
* [CWE-1022 window.opener 액세스가 있는 신뢰할 수 없는 대상에 대한 웹 링크 사용 (Use of Web Link to Untrusted Target with window.opener Access)](https://cwe.mitre.org/data/definitions/1022.html)
* [CWE-1125 과도한 공격 표면 (Excessive Attack Surface)](https://cwe.mitre.org/data/definitions/1125.html)


## X02:2025 메모리 관리 실패 (Memory Management Failures)

### 배경 (Background). 

Java, C#, JavaScript/TypeScript (node.js), Go 및 "안전한" Rust와 같은 언어는 메모리 안전합니다. 메모리 관리 문제는 C 및 C++와 같은 비메모리 안전 언어에서 발생하는 경향이 있습니다. 이 카테고리는 커뮤니티 설문조사에서 가장 낮은 점수를 받았고 데이터에서도 낮았지만 관련 CVE가 세 번째로 많았습니다. 우리는 이것이 더 전통적인 데스크톱 애플리케이션보다 웹 애플리케이션의 우세 때문이라고 믿습니다. 메모리 관리 취약점은 종종 가장 높은 CVSS 점수를 가집니다. 


### 점수 표 (Score table).


<table>
  <tr>
   <td>매핑된 CWE (CWEs Mapped) 
   </td>
   <td>최대 발생률 (Max Incidence Rate)
   </td>
   <td>평균 발생률 (Avg Incidence Rate)
   </td>
   <td>최대 커버리지 (Max Coverage)
   </td>
   <td>평균 커버리지 (Avg Coverage)
   </td>
   <td>평균 가중 악용 (Avg Weighted Exploit)
   </td>
   <td>평균 가중 영향 (Avg Weighted Impact)
   </td>
   <td>총 발생 횟수 (Total Occurrences)
   </td>
   <td>총 CVE (Total CVEs)
   </td>
  </tr>
  <tr>
   <td>24
   </td>
   <td>2.96%
   </td>
   <td>1.13%
   </td>
   <td>55.62%
   </td>
   <td>28.45%
   </td>
   <td>6.75
   </td>
   <td>4.82
   </td>
   <td>220,414
   </td>
   <td>30,978
   </td>
  </tr>
</table>



### 설명 (Description). 

애플리케이션이 메모리를 직접 관리하도록 강제될 때 실수를 하기가 매우 쉽습니다. 메모리 안전 언어가 더 자주 사용되고 있지만, 전 세계적으로 프로덕션에 있는 많은 레거시 시스템, 비메모리 안전 언어 사용을 요구하는 새로운 저수준 시스템, 그리고 메인프레임, IoT 장치, 펌웨어 및 자체 메모리를 관리하도록 강제될 수 있는 기타 시스템과 상호작용하는 웹 애플리케이션이 여전히 있습니다. 대표적인 CWE는 *CWE-120 입력 크기 확인 없이 버퍼 복사 ('클래식 버퍼 오버플로우', Buffer Copy without Checking Size of Input ('Classic Buffer Overflow'))* 및 *CWE-121 스택 기반 버퍼 오버플로우 (Stack-based Buffer Overflow)*입니다.

메모리 관리 실패는 다음 경우 발생할 수 있습니다:

* 변수에 대해 충분한 메모리를 할당하지 않는 경우
* 입력을 검증하지 않아 힙, 스택, 버퍼의 오버플로우를 초래하는 경우
* 변수 유형이 보유할 수 있는 것보다 큰 데이터 값을 저장하는 경우
* 할당되지 않은 메모리나 주소 공간을 사용하려고 시도하는 경우
* 오프 바이 원(off-by-one) 오류를 만드는 경우(0 대신 1부터 계산)
* 해제된 후 객체를 사용하려고 시도하는 경우
* 초기화되지 않은 변수를 사용하는 경우
* 메모리를 누수하거나 오류로 사용 가능한 모든 메모리를 사용하여 애플리케이션이 실패할 때까지 사용하는 경우

메모리 관리 실패는 애플리케이션 또는 전체 시스템의 실패로 이어질 수 있습니다. [X01:2025 애플리케이션 복원력 부족 (Lack of Application Resilience)](#x012025-lack-of-application-resilience)도 참조하세요.


### 예방 방법 (How to prevent). 

메모리 관리 실패를 방지하는 최선의 방법은 메모리 안전 언어를 사용하는 것입니다. 예에는 Rust, Java, Go, C#, Python, Swift, Kotlin, JavaScript 등이 포함됩니다. 새로운 애플리케이션을 만들 때, 조직이 메모리 안전 언어로 전환하는 학습 곡선이 가치가 있다고 설득하기 위해 노력하세요. 전체 리팩토링을 수행하는 경우, 가능하고 실현 가능할 때 메모리 안전 언어로 재작성을 추진하세요.

메모리 안전 언어를 사용할 수 없는 경우 다음을 수행하세요:

* 메모리 관리 오류 악용을 더 어렵게 만드는 다음 서버 기능을 활성화하세요: 주소 공간 레이아웃 무작위화(Address Space Layout Randomization, ASLR), 데이터 실행 보호(Data Execution Protection, DEP), 구조화된 예외 처리 덮어쓰기 보호(Structured Exception Handling Overwrite Protection, SEHOP).
* 애플리케이션에서 메모리 누수를 모니터링하세요.
* 시스템에 대한 모든 입력을 매우 신중하게 검증하고 예상에 맞지 않는 모든 입력을 거부하세요.
* 사용하는 언어를 연구하고 불안전하고 더 안전한 함수 목록을 만든 다음 전체 팀과 공유하세요. 가능한 경우, 보안 코딩 가이드라인이나 표준에 추가하세요. 예를 들어, C에서 strcpy()보다 strncpy()를 선호하고 strcat()보다 strncat()를 선호하세요.
* 언어나 프레임워크가 메모리 안전 라이브러리를 제공하는 경우 사용하세요. 예: Safestringlib 또는 SafeStr.
* 가능할 때마다 원시 배열과 포인터보다 관리되는 버퍼와 문자열을 사용하세요.
* 메모리 문제 및/또는 선택한 언어에 초점을 맞춘 보안 코딩 교육을 받으세요. 메모리 관리 실패에 대해 우려하고 있다고 교육자에게 알리세요.
* 코드 검토 및/또는 정적 분석을 수행하세요.
* StackShield, StackGuard 및 Libsafe와 같은 메모리 관리에 도움이 되는 컴파일러 도구를 사용하세요.
* 시스템의 모든 입력에 대해 퍼징을 수행하세요.
* 침투 테스트를 수행하는 경우, 메모리 관리 실패에 대해 우려하고 있으며 테스트 중에 이것에 특별한 주의를 기울이기를 원한다고 테스터에게 알리세요.
*  모든 컴파일러 오류 *및* 경고를 수정하세요. 프로그램이 컴파일되기 때문에 경고를 무시하지 마세요.
* 기본 인프라가 정기적으로 패치, 스캔 및 강화되도록 하세요.
* 잠재적인 메모리 취약점 및 기타 실패에 대해 기본 인프라를 특별히 모니터링하세요.
* 주소 스택을 오버플로우 공격으로부터 보호하기 위해 [카나리(canaries)](https://en.wikipedia.org/wiki/Buffer_overflow_protection#Canaries) 사용을 고려하세요.

### 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1:** 버퍼 오버플로우는 가장 유명한 메모리 취약점으로, 공격자가 필드가 수용할 수 있는 것보다 더 많은 정보를 제출하여 기본 변수에 대해 생성된 버퍼를 오버플로우시키는 상황입니다. 성공적인 공격에서 오버플로우 문자는 스택 포인터를 덮어쓰고 공격자가 프로그램에 악의적인 명령을 삽입할 수 있게 합니다.

**시나리오 #2:** 사용 후 해제(Use-After-Free, UAF)는 브라우저 버그 바운티 제출에서 반일반적으로 발생할 정도로 자주 발생합니다. DOM 요소를 조작하는 JavaScript를 처리하는 웹 브라우저를 상상해보세요. 공격자는 객체(예: DOM 요소)를 만들고 그것에 대한 참조를 얻는 JavaScript 페이로드를 만듭니다. 신중한 조작을 통해 그들은 브라우저가 객체의 메모리를 해제하도록 트리거하면서 그것에 대한 댕글링 포인터를 유지합니다. 브라우저가 메모리가 해제되었음을 인식하기 전에 공격자는 *동일한* 메모리 공간을 차지하는 새 객체를 할당합니다. 브라우저가 원래 포인터를 사용하려고 할 때, 그것은 이제 공격자가 제어하는 데이터를 가리킵니다. 이 포인터가 가상 함수 테이블용이었다면 공격자는 코드 실행을 페이로드로 리디렉션할 수 있습니다. 

**시나리오 #3:** 사용자 입력을 수락하고 적절하게 검증하거나 정제하지 않은 다음 로깅 함수에 직접 전달하는 네트워크 서비스. 사용자의 입력이 형식을 지정하지 않는 syslog(user_input) 대신 syslog("%s", user_input)로 로깅 함수에 전달됩니다. 공격자는 스택 메모리(민감한 데이터 공개)를 읽기 위해 %x와 같은 형식 지정자를 포함하거나 메모리 주소에 쓰기 위해 %n을 포함하는 악의적인 페이로드를 보냅니다. 여러 형식 지정자를 함께 연결하여 스택을 매핑하고 중요한 주소를 찾은 다음 덮어쓸 수 있습니다. 이것은 형식 문자열 취약점(제어되지 않은 문자열 형식)이 될 것입니다. 

참고: 현대 브라우저는 [브라우저 샌드박싱 (browser sandboxing)](https://www.geeksforgeeks.org/ethical-hacking/what-is-browser-sandboxing/#types-of-browser-sandboxing) ASLR, DEP/NX, RELRO 및 PIE를 포함하여 그러한 공격을 방어하기 위한 많은 수준의 방어를 사용합니다. 브라우저에 대한 메모리 관리 실패 공격은 수행하기 쉬운 공격이 아닙니다.

### 참고 자료 (References). 

* [OWASP 커뮤니티 페이지: 메모리 누수,](https://owasp.org/www-community/vulnerabilities/Memory_leak) [이중 메모리 해제,](https://owasp.org/www-community/vulnerabilities/Doubly_freeing_memory) [& 버퍼 오버플로우](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow)
* [Awesome Fuzzing: 퍼징 리소스 목록](https://github.com/secfigo/Awesome-Fuzzing) 
* [Project Zero 블로그](https://googleprojectzero.blogspot.com)
* [Microsoft MSRC 블로그](https://www.microsoft.com/en-us/msrc/blog)

## 매핑된 CWE 목록 (List of Mapped CWEs)
* [CWE-14 버퍼를 지우는 코드의 컴파일러 제거 (Compiler Removal of Code to Clear Buffers)](https://cwe.mitre.org/data/definitions/14.html)
* [CWE-119 메모리 버퍼 범위 내 작업의 부적절한 제한 (Improper Restriction of Operations within the Bounds of a Memory Buffer)](https://cwe.mitre.org/data/definitions/119.html)
* [CWE-120 입력 크기 확인 없이 버퍼 복사 ('클래식 버퍼 오버플로우', Buffer Copy without Checking Size of Input ('Classic Buffer Overflow'))](https://cwe.mitre.org/data/definitions/120.html)
* [CWE-121 스택 기반 버퍼 오버플로우 (Stack-based Buffer Overflow)](https://cwe.mitre.org/data/definitions/121.html)
* [CWE-122 힙 기반 버퍼 오버플로우 (Heap-based Buffer Overflow)](https://cwe.mitre.org/data/definitions/122.html)
* [CWE-124 버퍼 언더라이트 ('버퍼 언더플로우', Buffer Underwrite ('Buffer Underflow'))](https://cwe.mitre.org/data/definitions/124.html)
* [CWE-125 범위를 벗어난 읽기 (Out-of-bounds Read)](https://cwe.mitre.org/data/definitions/125.html)
* [CWE-126 버퍼 오버리드 (Buffer Over-read)](https://cwe.mitre.org/data/definitions/126.html)
* [CWE-190 정수 오버플로우 또는 래핑 (Integer Overflow or Wraparound)](https://cwe.mitre.org/data/definitions/190.html)
* [191 정수 언더플로우 (래핑 또는 래핑어라운드) (Integer Underflow (Wrap or Wraparound))](https://cwe.mitre.org/data/definitions/191.html)
* [CWE-196 부호 없는 것에서 부호 있는 것으로의 변환 오류 (Unsigned to Signed Conversion Error)](https://cwe.mitre.org/data/definitions/196.html)
* [CWE-367 확인 시점 사용 시점(TOCTOU) 경쟁 조건 (Time-of-check Time-of-use (TOCTOU) Race Condition)](https://cwe.mitre.org/data/definitions/367.html)
* [CWE-415 이중 해제 (Double Free)](https://cwe.mitre.org/data/definitions/415.html)
* [CWE-416 사용 후 해제 (Use After Free)](https://cwe.mitre.org/data/definitions/416.html)
* [CWE-457 초기화되지 않은 변수 사용 (Use of Uninitialized Variable)](https://cwe.mitre.org/data/definitions/457.html)
* [CWE-459 불완전한 정리 (Incomplete Cleanup)](https://cwe.mitre.org/data/definitions/459.html)
* [CWE-467 포인터 유형에 sizeof() 사용 (Use of sizeof() on a Pointer Type)](https://cwe.mitre.org/data/definitions/467.html)
* [CWE-787 범위를 벗어난 쓰기 (Out-of-bounds Write)](https://cwe.mitre.org/data/definitions/787.html)
* [CWE-788 버퍼 끝 이후 메모리 위치 액세스 (Access of Memory Location After End of Buffer)](https://cwe.mitre.org/data/definitions/788.html)
* [CWE-824 초기화되지 않은 포인터 액세스 (Access of Uninitialized Pointer)](https://cwe.mitre.org/data/definitions/824.html)
