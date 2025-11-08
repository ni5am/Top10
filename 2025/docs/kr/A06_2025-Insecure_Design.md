<link rel="stylesheet" href="../assets/css/RC-stylesheet.css" />

# A06:2025 불안전한 설계 (Insecure Design)


## 배경 (Background). 

불안전한 설계는 **[A02:2025-보안 설정 오류 (Security Misconfiguration)](A02_2025-Security_Misconfiguration.md)** 및 **[A03:2025-소프트웨어 공급망 실패 (Software Supply Chain Failures)](A03_2025-Software_Supply_Chain_Failures.md)**가 이를 추월하면서 순위에서 #4에서 #6으로 두 단계 하락했습니다. 이 카테고리는 2021년에 도입되었으며, 우리는 업계에서 위협 모델링과 보안 설계에 대한 더 큰 강조와 관련된 눈에 띄는 개선을 보았습니다. 이 카테고리는 설계 및 아키텍처 결함과 관련된 위험에 초점을 맞추며, 위협 모델링, 보안 설계 패턴 및 참조 아키텍처의 더 많은 사용을 요구합니다. 여기에는 애플리케이션의 비즈니스 로직 결함이 포함됩니다. 예: 애플리케이션 내에서 원하지 않거나 예상치 못한 상태 변경을 정의하는 부족. 커뮤니티로서 우리는 코딩 공간에서 "shift-left"를 넘어서 요구 사항 작성 및 애플리케이션 설계와 같은 코드 전 활동으로 이동해야 합니다. 이것은 설계 시 보안(Secure by Design) 원칙에 중요합니다(예: **[현대적 AppSec 프로그램 수립: 계획 및 설계 단계 (Establish a Modern AppSec Program: Planning and Design Phase)](0x03_2025-Establishing_a_Modern_Application_Security_Program.md)** 참조). 주목할 만한 공통 취약점 열거(Common Weakness Enumerations, CWEs)에는 *CWE-256: 자격 증명의 보호되지 않은 저장 (Unprotected Storage of Credentials), CWE-269 부적절한 권한 관리 (Improper Privilege Management), CWE-434 위험한 유형의 파일 무제한 업로드 (Unrestricted Upload of File with Dangerous Type), CWE-501: 신뢰 경계 위반 (Trust Boundary Violation), CWE-522: 불충분하게 보호된 자격 증명 (Insufficiently Protected Credentials)*이 포함됩니다.


## 점수 표 (Score table).


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
   <td>39
   </td>
   <td>22.18%
   </td>
   <td>1.86%
   </td>
   <td>88.76%
   </td>
   <td>35.18%
   </td>
   <td>6.96
   </td>
   <td>4.05
   </td>
   <td>729,882
   </td>
   <td>7,647
   </td>
  </tr>
</table>



## 설명 (Description). 

불안전한 설계는 "누락되거나 비효과적인 제어 설계"로 표현되는 다양한 약점을 나타내는 광범위한 카테고리입니다. 불안전한 설계는 다른 모든 Top 10 위험 카테고리의 원인이 아닙니다. 불안전한 설계와 불안전한 구현 사이에는 차이가 있다는 점에 유의하세요. 우리가 설계 결함과 구현 결함을 구분하는 이유가 있습니다. 그들은 다른 근본 원인을 가지고, 개발 프로세스의 다른 시점에 발생하며, 다른 수정 방법을 가지고 있습니다. 안전한 설계도 여전히 악용될 수 있는 취약점으로 이어지는 구현 결함을 가질 수 있습니다. 불안전한 설계는 필요한 보안 제어가 특정 공격에 대해 방어하기 위해 만들어지지 않았기 때문에 완벽한 구현으로 수정할 수 없습니다. 불안전한 설계에 기여하는 요인 중 하나는 개발 중인 소프트웨어 또는 시스템에 내재된 비즈니스 위험 프로파일링의 부족과 따라서 어떤 수준의 보안 설계가 필요한지 결정하는 실패입니다.

안전한 설계를 갖는 세 가지 핵심 부분은 다음과 같습니다:

* 요구 사항 및 리소스 관리 수집
* 안전한 설계 생성
* 안전한 개발 수명 주기 보유


### 요구 사항 및 리소스 관리 (Requirements and Resource Management)

비즈니스와 함께 애플리케이션에 대한 비즈니스 요구 사항을 수집하고 협상하세요. 여기에는 모든 데이터 자산의 기밀성, 무결성, 가용성 및 진정성에 관한 보호 요구 사항과 예상 비즈니스 로직이 포함됩니다. 애플리케이션이 얼마나 노출될 것인지, 테넌트 분리가 필요한지(접근 제어에 필요한 것 이상)를 고려하세요. 기능적 및 비기능적 보안 요구 사항을 포함한 기술 요구 사항을 컴파일하세요. 설계, 구축, 테스트 및 운영을 포함한 모든 것을 포함하는 예산을 계획하고 협상하세요. 여기에는 보안 활동이 포함됩니다.


### 안전한 설계 (Secure Design)

안전한 설계는 지속적으로 위협을 평가하고 코드가 알려진 공격 방법을 방지하도록 강력하게 설계되고 테스트되도록 보장하는 문화 및 방법론입니다. 위협 모델링은 정제 세션(또는 유사한 활동)에 통합되어야 합니다. 데이터 흐름 및 접근 제어 또는 기타 보안 제어의 변경을 찾으세요. 사용자 스토리 개발에서 올바른 흐름과 실패 상태를 결정하고, 책임 있는 당사자와 영향을 받는 당사자가 잘 이해하고 동의하는지 확인하세요. 예상 흐름과 실패 흐름에 대한 가정과 조건을 분석하여 정확하고 바람직한 상태로 유지되는지 확인하세요. 가정을 검증하고 적절한 동작에 필요한 조건을 강제하는 방법을 결정하세요. 결과가 사용자 스토리에 문서화되어 있는지 확인하세요. 실수로부터 배우고 개선을 촉진하기 위한 긍정적인 인센티브를 제공하세요. 안전한 설계는 소프트웨어에 추가할 수 있는 추가 기능이나 도구가 아닙니다.


### 안전한 개발 수명 주기 (Secure Development Lifecycle)

안전한 소프트웨어는 안전한 개발 수명 주기, 안전한 설계 패턴, 포장된 도로 방법론, 안전한 구성 요소 라이브러리, 적절한 도구, 위협 모델링 및 프로세스를 개선하는 데 사용되는 사고 사후 분석을 필요로 합니다. 소프트웨어 프로젝트의 시작, 프로젝트 전반, 그리고 지속적인 소프트웨어 유지보수를 위해 보안 전문가에게 연락하세요. 안전한 소프트웨어 개발 노력을 구조화하는 데 도움이 되도록 [OWASP 소프트웨어 보증 성숙도 모델 (Software Assurance Maturity Model, SAMM)](https://owaspsamm.org/)을 활용하는 것을 고려하세요.


## 예방 방법 (How to prevent). 



* AppSec 전문가와 함께 보안 및 개인정보 보호 관련 제어를 평가하고 설계하는 데 도움이 되는 안전한 개발 수명 주기를 수립하고 사용하세요.
* 안전한 설계 패턴 또는 포장된 도로 구성 요소 라이브러리를 수립하고 사용하세요.
* 인증, 접근 제어, 비즈니스 로직 및 주요 흐름과 같은 애플리케이션의 중요한 부분에 대해 위협 모델링을 사용하세요.
* 사용자 스토리에 보안 언어 및 제어를 통합하세요.
* 애플리케이션의 각 계층(프론트엔드에서 백엔드까지)에서 타당성 검사를 통합하세요.
* 모든 중요한 흐름이 위협 모델에 저항력이 있다는 것을 검증하기 위해 단위 및 통합 테스트를 작성하세요. 애플리케이션의 각 계층에 대해 사용 사례 *및* 오용 사례를 컴파일하세요.
* 노출 및 보호 요구에 따라 시스템 및 네트워크 계층에서 계층을 분리하세요.
* 모든 계층에 걸쳐 설계에 의해 테넌트를 강력하게 분리하세요.


## 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1:** 자격 증명 복구 워크플로우에 "질문과 답변"이 포함될 수 있으며, 이것은 NIST 800-63b, OWASP ASVS 및 OWASP Top 10에서 금지됩니다. 질문과 답변은 둘 이상의 사람이 답을 알 수 있기 때문에 신원 증거로 신뢰할 수 없습니다. 이러한 기능은 제거되고 더 안전한 설계로 교체되어야 합니다.

**시나리오 #2:** 영화관 체인이 그룹 예약 할인을 허용하고 보증금을 요구하기 전에 최대 15명의 참석자를 허용합니다. 공격자는 이 흐름을 위협 모델링하고 애플리케이션의 비즈니스 로직에서 공격 벡터를 찾을 수 있는지 테스트할 수 있습니다. 예: 몇 번의 요청으로 600석과 모든 영화관을 한 번에 예약하여 수입의 대규모 손실을 초래합니다.

**시나리오 #3:** 소매 체인의 전자상거래 웹사이트는 경매 웹사이트에서 재판매하기 위해 고급 비디오 카드를 구매하는 스캘퍼가 운영하는 봇에 대한 보호가 없습니다. 이것은 비디오 카드 제조업체와 소매 체인 소유자에게 끔찍한 홍보를 만들고, 어떤 가격으로도 이러한 카드를 얻을 수 없는 애호가들과 지속적인 악감정을 만듭니다. 가용성 후 몇 초 내에 이루어진 구매와 같은 신중한 봇 방지 설계 및 도메인 로직 규칙은 비정품 구매를 식별하고 이러한 거래를 거부할 수 있습니다.


## 참고 자료 (References). 



* [OWASP 치트 시트: 안전한 설계 원칙 (OWASP Cheat Sheet: Secure Design Principles)](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html)
* [OWASP SAMM: 설계 | 안전한 아키텍처 (OWASP SAMM: Design | Secure Architecture)](https://owaspsamm.org/model/design/secure-architecture/)
* [OWASP SAMM: 설계 | 위협 평가 (OWASP SAMM: Design | Threat Assessment)](https://owaspsamm.org/model/design/threat-assessment/)
* [NIST – 개발자 소프트웨어 검증을 위한 최소 표준 가이드라인 (NIST – Guidelines on Minimum Standards for Developer Verification of Software)](https://www.nist.gov/publications/guidelines-minimum-standards-developer-verification-software)
* [위협 모델링 선언문 (The Threat Modeling Manifesto)](https://threatmodelingmanifesto.org/)
* [Awesome 위협 모델링 (Awesome Threat Modeling)](https://github.com/hysnsec/awesome-threat-modelling)


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-73 파일 이름 또는 경로의 외부 제어 (External Control of File Name or Path)](https://cwe.mitre.org/data/definitions/73.html)

* [CWE-183 허용된 입력의 허용적 목록 (Permissive List of Allowed Inputs)](https://cwe.mitre.org/data/definitions/183.html)

* [CWE-256 자격 증명의 보호되지 않은 저장 (Unprotected Storage of Credentials)](https://cwe.mitre.org/data/definitions/256.html)

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

* [CWE-444 HTTP 요청의 일관성 없는 해석 ('HTTP 요청 스머글링', Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling'))](https://cwe.mitre.org/data/definitions/444.html)

* [CWE-451 사용자 인터페이스(UI)의 중요한 정보 잘못된 표현 (User Interface (UI) Misrepresentation of Critical Information)](https://cwe.mitre.org/data/definitions/451.html)

* [CWE-454 신뢰할 수 있는 변수 또는 데이터 저장소의 외부 초기화 (External Initialization of Trusted Variables or Data Stores)](https://cwe.mitre.org/data/definitions/454.html)

* [CWE-472 가정된 불변 웹 매개변수의 외부 제어 (External Control of Assumed-Immutable Web Parameter)](https://cwe.mitre.org/data/definitions/472.html)

* [CWE-501 신뢰 경계 위반 (Trust Boundary Violation)](https://cwe.mitre.org/data/definitions/501.html)

* [CWE-522 불충분하게 보호된 자격 증명 (Insufficiently Protected Credentials)](https://cwe.mitre.org/data/definitions/522.html)

* [CWE-525 민감한 정보를 포함하는 웹 브라우저 캐시 사용 (Use of Web Browser Cache Containing Sensitive Information)](https://cwe.mitre.org/data/definitions/525.html)

* [CWE-539 민감한 정보를 포함하는 영구 쿠키 사용 (Use of Persistent Cookies Containing Sensitive Information)](https://cwe.mitre.org/data/definitions/539.html)

* [CWE-598 민감한 쿼리 문자열이 있는 GET 요청 메서드 사용 (Use of GET Request Method With Sensitive Query Strings)](https://cwe.mitre.org/data/definitions/598.html)

* [CWE-602 서버 측 보안의 클라이언트 측 강제 (Client-Side Enforcement of Server-Side Security)](https://cwe.mitre.org/data/definitions/602.html)

* [CWE-628 잘못 지정된 인수가 있는 함수 호출 (Function Call with Incorrectly Specified Arguments)](https://cwe.mitre.org/data/definitions/628.html)

* [CWE-642 중요한 상태 데이터의 외부 제어 (External Control of Critical State Data)](https://cwe.mitre.org/data/definitions/642.html)

* [CWE-646 외부에서 제공된 파일의 파일 이름 또는 확장자에 대한 의존 (Reliance on File Name or Extension of Externally-Supplied File)](https://cwe.mitre.org/data/definitions/646.html)

* [CWE-653 불충분한 구획화 (Insufficient Compartmentalization)](https://cwe.mitre.org/data/definitions/653.html)

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
