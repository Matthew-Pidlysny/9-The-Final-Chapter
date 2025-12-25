/*
 * Kardashev Suite - File Type System Definition
 * Round 1: Foundation Implementation
 * 
 * Defines .k1 through .k5 file type standards for Kardashev-level software evaluation
 */

#ifndef KARDASHEV_FILE_TYPES_H
#define KARDASHEV_FILE_TYPES_H

#include <string>
#include <vector>
#include <map>
#include <memory>

namespace KardashevSuite {

/**
 * Kardashev Level Enumeration
 * Represents the 5 levels of software sophistication
 */
enum class KardashevLevel {
    K1 = 1,  // Basic Industrial Software
    K2 = 2,  // Advanced Enterprise Systems  
    K3 = 3,  // AI-Enhanced Applications
    K4 = 4,  // Quantum-Ready Systems
    K5 = 5   // Type V Multiversal Software
};

/**
 * File Type Metadata Structure
 * Contains all necessary information for Kardashev file evaluation
 */
struct KardashevFileMetadata {
    KardashevLevel level;
    std::string version;
    std::string author;
    std::string description;
    std::vector<std::string> dependencies;
    std::map<std::string, std::string> properties;
    uint64_t creation_timestamp;
    uint64_t last_modified;
    std::string checksum;
};

/**
 * Kardashev File Base Class
 * Abstract interface for all Kardashev file types
 */
class KardashevFile {
public:
    virtual ~KardashevFile() = default;
    
    // Core file operations
    virtual bool load(const std::string& filepath) = 0;
    virtual bool save(const std::string& filepath) = 0;
    virtual bool validate() = 0;
    
    // Metadata operations
    virtual KardashevFileMetadata get_metadata() const = 0;
    virtual void set_metadata(const KardashevFileMetadata& metadata) = 0;
    
    // Evaluation operations
    virtual double evaluate_quality() = 0;
    virtual std::vector<std::string> get_evaluation_criteria() = 0;
    
    // Dependency management
    virtual std::vector<std::string> get_dependencies() const = 0;
    virtual bool add_dependency(const std::string& dependency) = 0;
    virtual bool remove_dependency(const std::string& dependency) = 0;
    
protected:
    KardashevFileMetadata metadata_;
};

/**
 * Template Implementation for Each Kardashev Level
 */
template<KardashevLevel Level>
class KardashevFileImpl : public KardashevFile {
public:
    KardashevFileImpl();
    
    // Implementation of virtual methods
    bool load(const std::string& filepath) override;
    bool save(const std::string& filepath) override;
    bool validate() override;
    
    KardashevFileMetadata get_metadata() const override { return metadata_; }
    void set_metadata(const KardashevFileMetadata& metadata) override { metadata_ = metadata; }
    
    double evaluate_quality() override;
    std::vector<std::string> get_evaluation_criteria() override;
    
    std::vector<std::string> get_dependencies() const override { return metadata_.dependencies; }
    bool add_dependency(const std::string& dependency) override;
    bool remove_dependency(const std::string& dependency) override;
    
    // Level-specific methods
    static constexpr KardashevLevel get_level() { return Level; }
    static std::string get_file_extension();
    static std::string get_level_description();
    
private:
    std::vector<uint8_t> file_data_;
    bool is_loaded_;
    
    // Level-specific validation
    bool validate_level_specific();
};

// Type aliases for each level
using K1File = KardashevFileImpl<KardashevLevel::K1>;
using K2File = KardashevFileImpl<KardashevLevel::K2>;
using K3File = KardashevFileImpl<KardashevLevel::K3>;
using K4File = KardashevFileImpl<KardashevLevel::K4>;
using K5File = KardashevFileImpl<KardashevLevel::K5>;

/**
 * File Factory for creating appropriate file types
 */
class KardashevFileFactory {
public:
    static std::unique_ptr<KardashevFile> create_file(KardashevLevel level);
    static std::unique_ptr<KardashevFile> create_file_from_extension(const std::string& extension);
    static KardashevLevel detect_level_from_filename(const std::string& filename);
};

} // namespace KardashevSuite

#endif // KARDASHEV_FILE_TYPES_H