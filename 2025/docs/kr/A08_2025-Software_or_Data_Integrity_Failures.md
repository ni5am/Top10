<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

# A08:2025 소프트웨어 또는 데이터 무결성 실패 (Software or Data Integrity Failures) ![icon](../../assets/TOP_10_Icons_Final_Software_and_Data_Integrity_Failures.png){: style="height:80px;width:80px" align="right"}

## 배경 (Background). 

소프트웨어 또는 데이터 무결성 실패는 "소프트웨어 *및* 데이터 무결성 실패 (Software *and* Data Integrity Failures)"에서 약간의 명확화된 이름 변경과 함께 #8을 계속 유지합니다. 이 카테고리는 소프트웨어 공급망 실패(Software Supply Chain Failures)보다 낮은 수준에서 소프트웨어, 코드, 데이터 아티팩트의 무결성을 검증하고 신뢰 경계를 유지하는 실패에 초점을 맞춥니다. 이 카테고리는 무결성을 검증하지 않고 소프트웨어 업데이트 및 중요한 데이터와 관련된 가정을 만드는 것에 초점을 맞춥니다. 주목할 만한 공통 취약점 열거(Common Weakness Enumerations, CWEs)에는 *CWE-829: 신뢰할 수 없는 제어 영역에서 기능 포함 (Inclusion of Functionality from Untrusted Control Sphere)*, *CWE-915: 동적으로 결정된 객체 속성의 부적절하게 제어된 수정 (Improperly Controlled Modification of Dynamically-Determined Object Attributes)*, *CWE-502: 신뢰할 수 없는 데이터의 역직렬화 (Deserialization of Untrusted Data)*가 포함됩니다.


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
   <td>14
   </td>
   <td>8.98%
   </td>
   <td>2.75%
   </td>
   <td>78.52%
   </td>
   <td>45.49%
   </td>
   <td>7.11
   </td>
   <td>4.79
   </td>
   <td>501,327
   </td>
   <td>3,331
   </td>
  </tr>
</table>



## 설명 (Description). 

소프트웨어 및 데이터 무결성 실패는 잘못되었거나 신뢰할 수 없는 코드나 데이터가 신뢰할 수 있고 유효한 것으로 처리되는 것을 방지하지 않는 코드 및 인프라와 관련이 있습니다. 이것의 예는 애플리케이션이 신뢰할 수 없는 소스, 저장소 및 콘텐츠 전송 네트워크(Content Delivery Networks, CDN)의 플러그인, 라이브러리 또는 모듈에 의존하는 경우입니다. 소프트웨어 무결성 검사를 소비하고 제공하지 않는 불안전한 CI/CD 파이프라인은 무단 액세스, 불안전하거나 악의적인 코드, 또는 시스템 손상의 가능성을 도입할 수 있습니다. 이것에 대한 또 다른 예는 신뢰할 수 없는 장소에서 코드나 아티팩트를 가져오고/또는 사용하기 전에 검증하지 않는(서명 또는 유사한 메커니즘을 확인하여) CI/CD입니다. 마지막으로, 많은 애플리케이션이 이제 자동 업데이트 기능을 포함하며, 여기서 업데이트는 충분한 무결성 검증 없이 다운로드되어 이전에 신뢰할 수 있었던 애플리케이션에 적용됩니다. 공격자는 잠재적으로 모든 설치에서 배포되고 실행될 자체 업데이트를 업로드할 수 있습니다. 또 다른 예는 객체나 데이터가 공격자가 보고 수정할 수 있는 구조로 인코딩되거나 직렬화되는 경우 불안전한 역직렬화에 취약한 경우입니다.


## 예방 방법 (How to prevent). 



* 소프트웨어나 데이터가 예상 소스에서 왔고 변경되지 않았는지 검증하기 위해 디지털 서명 또는 유사한 메커니즘을 사용하세요.
* npm 또는 Maven과 같은 라이브러리 및 종속성이 신뢰할 수 있는 저장소만 소비하도록 하세요. 더 높은 위험 프로필이 있는 경우, 검증된 내부 알려진 양호 저장소를 호스팅하는 것을 고려하세요.
* 악의적인 코드나 구성이 소프트웨어 파이프라인에 도입될 가능성을 최소화하기 위해 코드 및 구성 변경에 대한 검토 프로세스가 있는지 확인하세요.
* 빌드 및 배포 프로세스를 통해 흐르는 코드의 무결성을 보장하기 위해 CI/CD 파이프라인에 적절한 분리, 구성 및 접근 제어가 있는지 확인하세요.
* 서명되지 않았거나 암호화되지 않은 직렬화된 데이터가 신뢰할 수 없는 클라이언트로부터 수신되고 직렬화된 데이터의 변조나 재생을 탐지하기 위한 어떤 형태의 무결성 검사나 디지털 서명 없이 사용되지 않는지 확인하세요.


## 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1 신뢰할 수 없는 소스에서 웹 기능 포함:** 회사가 지원 기능을 제공하기 위해 외부 서비스 제공자를 사용합니다. 편의를 위해 `myCompany.SupportProvider.com`에 대한 DNS 매핑이 `support.myCompany.com`으로 설정되어 있습니다. 이것은 `myCompany.com` 도메인에 설정된 모든 쿠키(인증 쿠키 포함)가 이제 지원 제공자에게 전송됨을 의미합니다. 지원 제공자의 인프라에 액세스할 수 있는 모든 사람은 `support.myCompany.com`을 방문한 모든 사용자의 쿠키를 훔치고 세션 하이재킹 공격을 수행할 수 있습니다.

**시나리오 #2 서명 없이 업데이트:** 많은 홈 라우터, 셋톱 박스, 장치 펌웨어 및 기타는 서명된 펌웨어를 통해 업데이트를 검증하지 않습니다. 서명되지 않은 펌웨어는 공격자에게 점점 더 많은 표적이 되고 있으며 더 악화될 것으로 예상됩니다. 이것은 많은 경우 미래 버전에서 수정하고 이전 버전이 오래될 때까지 기다리는 것 외에는 수정 메커니즘이 없기 때문에 주요 관심사입니다.

시나리오 #2 개발자가 찾고 있는 패키지의 업데이트된 버전을 찾는 데 어려움을 겪어 정기적인 신뢰할 수 있는 패키지 관리자가 아닌 온라인 웹사이트에서 다운로드합니다. 패키지가 서명되지 않았으므로 무결성을 보장할 기회가 없습니다. 패키지에 악의적인 코드가 포함되어 있습니다. 

**시나리오 #3 불안전한 역직렬화:** React 애플리케이션이 Spring Boot 마이크로서비스 세트를 호출합니다. 함수형 프로그래머로서 그들은 코드가 불변인지 확인하려고 시도했습니다. 그들이 생각해낸 해결책은 사용자 상태를 직렬화하고 각 요청과 함께 앞뒤로 전달하는 것입니다. 공격자는 "rO0" Java 객체 서명(base64)을 발견하고 [Java 역직렬화 스캐너 (Java Deserialization Scanner)](https://github.com/federicodotta/Java-Deserialization-Scanner)를 사용하여 애플리케이션 서버에서 원격 코드 실행을 얻습니다.

## 참고 자료 (References). 

* [OWASP 치트 시트: 소프트웨어 공급망 보안 (OWASP Cheat Sheet: Software Supply Chain Security)](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html)
* [OWASP 치트 시트: 코드로서의 인프라 (OWASP Cheat Sheet: Infrastructure as Code)](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html)
* [OWASP 치트 시트: 역직렬화 (OWASP Cheat Sheet: Deserialization)](https://wiki.owasp.org/index.php/Deserialization_Cheat_Sheet)
* [SAFECode 소프트웨어 무결성 제어 (SAFECode Software Integrity Controls)](https://safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf)
* ['최악의 악몽' 사이버 공격: SolarWinds 해킹의 알려지지 않은 이야기 (A 'Worst Nightmare' Cyberattack: The Untold Story Of The SolarWinds Hack)](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack)
* [CodeCov Bash 업로더 손상 (CodeCov Bash Uploader Compromise)](https://about.codecov.io/security-update)
* [Julien Vehent의 Securing DevOps](https://www.manning.com/books/securing-devops)
* [Tenendo의 불안전한 역직렬화 (Insecure Deserialization by Tenendo)](https://tenendo.com/insecure-deserialization/)


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-345 데이터 진정성의 불충분한 검증 (Insufficient Verification of Data Authenticity)](https://cwe.mitre.org/data/definitions/345.html)

* [CWE-353 무결성 검사에 대한 지원 누락 (Missing Support for Integrity Check)](https://cwe.mitre.org/data/definitions/353.html)

* [CWE-426 신뢰할 수 없는 검색 경로 (Untrusted Search Path)](https://cwe.mitre.org/data/definitions/426.html)

* [CWE-427 제어되지 않은 검색 경로 요소 (Uncontrolled Search Path Element)](https://cwe.mitre.org/data/definitions/427.html)

* [CWE-494 무결성 검사 없이 코드 다운로드 (Download of Code Without Integrity Check)](https://cwe.mitre.org/data/definitions/494.html)

* [CWE-502 신뢰할 수 없는 데이터의 역직렬화 (Deserialization of Untrusted Data)](https://cwe.mitre.org/data/definitions/502.html)

* [CWE-506 포함된 악의적인 코드 (Embedded Malicious Code)](https://cwe.mitre.org/data/definitions/506.html)

* [CWE-509 악의적인 코드 복제 (바이러스 또는 웜, Replicating Malicious Code (Virus or Worm))](https://cwe.mitre.org/data/definitions/509.html)

* [CWE-565 검증 및 무결성 검사 없이 쿠키에 대한 의존 (Reliance on Cookies without Validation and Integrity Checking)](https://cwe.mitre.org/data/definitions/565.html)

* [CWE-784 보안 결정에서 검증 및 무결성 검사 없이 쿠키에 대한 의존 (Reliance on Cookies without Validation and Integrity Checking in a Security Decision)](https://cwe.mitre.org/data/definitions/784.html)

* [CWE-829 신뢰할 수 없는 제어 영역에서 기능 포함 (Inclusion of Functionality from Untrusted Control Sphere)](https://cwe.mitre.org/data/definitions/829.html)

* [CWE-830 신뢰할 수 없는 소스에서 웹 기능 포함 (Inclusion of Web Functionality from an Untrusted Source)](https://cwe.mitre.org/data/definitions/830.html)

* [CWE-915 동적으로 결정된 객체 속성의 부적절하게 제어된 수정 (Improperly Controlled Modification of Dynamically-Determined Object Attributes)](https://cwe.mitre.org/data/definitions/915.html)

* [CWE-926 Android 애플리케이션 구성 요소의 부적절한 내보내기 (Improper Export of Android Application Components)](https://cwe.mitre.org/data/definitions/926.html)
